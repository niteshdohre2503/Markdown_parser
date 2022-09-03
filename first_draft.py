from tkinter import * 
import tkinter as tk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
import regex as re
from __init__ import *
import os
from PIL import ImageTk, Image


global edit_this_var
def reg(result):
    #heading h1
    regex_h1 = r"^(#\s)(.*)"
    subst_h1 = "<h1>\\2</h1>"
  
    #heading h2
    regex_h2 = r"^(##\s)(.*)"
    subst_h2 = "<h2>\\2</h2>"

    #heading h3
    regex_h3 = r"^(###\s)(.*)"
    subst_h3 = "<h3>\\2</h3>"

    #bold and itlatics
    regex_ib = r"(\*\*\*)(\b)([^\*]*)(\b)(\*\*\*)"
    subst_ib = "<em><b>\\3</b></em>"

    #bold
    regex_b = r"(\*\*)(\b)([^\*]*)(\b)(\*\*)"
    subst_b = "<b>\\3</b>"

    #italics
    regex_i = r"(\*)(\b)([^\*]*)(\b)(\*)"
    subst_i = "<em>\\3</em>"


    result = re.sub(regex_h1, subst_h1, result, 0, re.MULTILINE)
    result = re.sub(regex_h2, subst_h2, result, 0, re.MULTILINE)
    result = re.sub(regex_h3, subst_h3, result, 0, re.MULTILINE)
    result = re.sub(regex_ib, subst_ib, result, 0, re.MULTILINE)
    result = re.sub(regex_b, subst_b, result, 0, re.MULTILINE)
    result = re.sub(regex_i, subst_i, result, 0, re.MULTILINE)

    
    return result


def read_file():
    global edit
    edit=True
    global edit_this_var

    edit_this_var=None
    print("read file was called\n")
    text_file =askopenfilename(initialdir = "E:\SL_Project_mywiki\COP702_1\database_SL",title = "Select a File",filetypes = (("Markup Documents", "*.md"),("all files", "*.*")))
    edit_this_var=text_file
    text_file=open(text_file,'r' )
    stuff=text_file.read()

    if stuff!="":
        stuff=reg(stuff)
        Read_renderer.set_html(stuff)
    else:
        Read_renderer.set_html("This article is <b>blank</b>, you can edit though !!")



def save_file_as():    
    try:
        path = filedialog.asksaveasfile(filetypes = (("MD File", "*.md"), ("All files", "*.*"))).name
        root.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(text_area.get('1.0', tk.END))


def inputEditorChange(event):
    text_area.edit_modified(0)
    markdownText = text_area.get("1.0", "end")
    html = reg(markdownText)
    Label_renderer.set_html(html)

def edit_file():
    global edit_this_var

    if edit==True:
        edit_this_var=open(edit_this_var,'r' )
        stuff=edit_this_var.read()
        text_area.delete(1.0, END)
        text_area.insert(1.0,stuff)


root=Tk()
root.title("MY WIKI")
root.geometry("1460x820")
root.wm_iconbitmap("1.ico")


# frames ###############################################################################################################

top_frame=LabelFrame(root, width=1460, height= 70, bg="light blue")
top_frame.place(x=0,y=0)

left_frame=LabelFrame(root, width=300, height=750)
left_frame.place(x=0, y=70)

middle_frame=LabelFrame(root, width=580, height=750)
middle_frame.place(x=300, y=70)

right_frame_1=LabelFrame(root, width=580, height=375)
right_frame_1.place(x=880, y=70)

right_frame_3=LabelFrame(root, width=580, height=375)
right_frame_3.place(x=880, y=460)

# frames end###########################################################################################################


img = Image.open("1.png")
resize_img = img.resize((60 ,60))
img = ImageTk.PhotoImage(resize_img)
image_label=Label(image=img)
image_label.pack()
heading=Label(top_frame, text="OUR            PEDIA", font="ARIAL 34 bold", bg="light green")
heading.pack()



#menubar###############################################################################################################
mainmenu=Menu(root)
mainmenu.add_command(label=" Save ", command=save_file_as)
mainmenu.add_command(label=" Edit ", command=edit_file)
mainmenu.add_command(label="OPEN",command=read_file)


root.config(menu=mainmenu)
#######################################################################################################################


# populating right frame 1#############################################################################################

text_area=scrolledtext.ScrolledText(right_frame_1, wrap=tk.WORD ,bg="gray", fg="white", font="arial 15", insertofftime=5, 
                                        insertontime=15, width=200)
text_area.pack()
text_area.bind("<<Modified>>", inputEditorChange)

Label_renderer=HTMLLabel(right_frame_3, html="<h1>Type Above in the Textbox</h1>", background="lightblue")
Label_renderer.pack()

Read_renderer=HTMLLabel(middle_frame, html="Here the selected article will appear", width=300, height=750, background="lightpink", fg="white",
                 container=Read_renderer)
Read_renderer.pack()

#######################################################################################################################


# Populating left frame.###############################################################################################

left_label=HTMLScrolledText(left_frame)

path="E:\SL_Project_mywiki\COP702_1\database_SL"
dir_list=os.listdir(path)

list_of_articles="<h2> LIST OF ARTICLES </h2>"
for x in dir_list:
    if x.endswith(".md"):
        list_of_articles= list_of_articles + f"<a href='{path}\{x}'> {x[:-3]} </a><br>"

left_label.set_html(list_of_articles)
left_label.configure(state='disabled')
left_label.pack()

######################################################################################################################


root.mainloop()