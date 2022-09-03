from tkinter import * 
import tkinter as tk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
import regex as re
from __init__ import *
import os
from PIL import ImageTk, Image
from md_to_html import reg

class Finally(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("MY WIKI")
        self.geometry("1460x820")
        self.wm_iconbitmap("1.ico")

        
        self.edit_this_var=None
        self.edit=None

        self.initializeFrames()
        self.initialize_top_frame()
        self.initialize_left_frame()
        self.initialize_right_frame()
        self.initialize_middle_frame()
        self.initialize_menu()



        self.mainloop()
    
  



    def save_file_as(self):    
        try:
            path = filedialog.asksaveasfile(filetypes = (("MD File", "*.md"), ("All files", "*.*"))).name
            self.title('Notepad - ' + path)
        
        except:
            return   
        
        with open(path, 'w') as f:
            f.write(self.text_area.get('1.0', tk.END))


    def inputEditorChange(self,event):
        self.text_area.edit_modified(0)
        markdownText = self.text_area.get("1.0", "end")
        html = reg(markdownText)
        self.Label_renderer.set_html(html)

    def edit_file(self):
       if self.edit==True:
            self.edit_this_var=open(self.edit_this_var,'r' )
            stuff=self.edit_this_var.read()
            self.text_area.delete(1.0, END)
            self.text_area.insert(1.0,stuff)


    # frames ###############################################################################################################

    def initializeFrames(self):
        self.top_frame=LabelFrame(self, width=1460, height= 70, bg="light blue")
        self.top_frame.place(x=0,y=0)

        self.left_frame=LabelFrame(self, width=300, height=750)
        self.left_frame.place(x=0, y=70)

        self.middle_frame=LabelFrame(self, width=580, height=750)
        self.middle_frame.place(x=300, y=70)

        self.right_frame_1=LabelFrame(self, width=580, height=375)
        self.right_frame_1.place(x=880, y=70)

        self.right_frame_3=LabelFrame(self, width=580, height=375)
        self.right_frame_3.place(x=880, y=460)

# frames end###########################################################################################################


    def initialize_top_frame(self):
        img = Image.open("1.png")
        resize_img = img.resize((60 ,60))
        img = ImageTk.PhotoImage(resize_img)
        image_label=Label(image=img)
        image_label.pack()
        heading=Label(self.top_frame, text="OUR            PEDIA", font="ARIAL 34 bold", bg="light green")
        heading.pack()



    #menubar###############################################################################################################
    def initialize_menu(self):
        mainmenu=Menu(self)
        mainmenu.add_command(label=" Save ", command=self.save_file_as)
        mainmenu.add_command(label=" Edit ", command=self.edit_file)


        self.config(menu=mainmenu)
    #######################################################################################################################



    # populating right frame 1#############################################################################################

    def initialize_right_frame(self):
        self.text_area=scrolledtext.ScrolledText(self.right_frame_1, wrap=tk.WORD ,bg="gray", fg="white", font="arial 15", insertofftime=5, 
                                            insertontime=15, width=200)
        self.text_area.pack()
        self.text_area.bind("<<Modified>>", self.inputEditorChange)

        self.Label_renderer=HTMLLabel(self.right_frame_3, html="<h1>Type Above in the Textbox</h1>", background="lightblue")
        self.Label_renderer.pack()


    #######################################################################################################################
    def initialize_middle_frame(self):
        
        self.Read_renderer=HTMLScrolledText(self.middle_frame, html="Here the selected article will appear",container=self, width=300, height=750, 
                                     background="lightpink", fg="white",state="disabled")
        self.Read_renderer.pack()

    # Populating left frame.###############################################################################################
    def initialize_left_frame(self):
        self.left_label=HTMLScrolledText(self.left_frame, container=self)

        path="E:\SL_Project_mywiki\COP702_1\database_SL"
        dir_list=os.listdir(path)

        list_of_articles="<h2> LIST OF ARTICLES </h2>"
        for x in dir_list:
            if x.endswith(".md"):
                list_of_articles= list_of_articles + f"<a href='{path}\{x}'> {x[:-3]} </a><br>"

        self.left_label.set_html(list_of_articles)
        self.left_label.configure(state='disabled')
        self.left_label.pack()

    ######################################################################################################################

Finally()