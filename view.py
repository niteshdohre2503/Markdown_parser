from email.mime import image
from tkinter import * 
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from __init__ import *
import os
from PIL import ImageTk, Image
from md_to_html import reg

class View(tk.Tk):

    
    def __init__(self,controller): 
        super().__init__()
        self.controller = controller
        self.title("MY WIKI")
        self.geometry("1460x820")
        self.wm_iconbitmap("1.ico")

        
        self.edit_this_var=""
        self.edit=False
        self.opened=False
        
        

        self.initializeFrames()
        self.initialize_top_frame()
        self.initialize_middle_frame()
        self.initialize_right_frame()
        self.initialize_left_frame()
        self.initialize_menu()



        self.mainloop()


    '''function use to save files, there are two cases encountered here, i) when a file was opened in the middle frame and also the edit 
       command was activated, in this case the selected file will just be overwritten with what is newly edited.
       ii) when a new file is being created.
    '''
    def save_file_as(self):   
        if self.edit==True and self.opened==True:

            self.edit=False
            
           
            with open(self.edit_this_var, 'r+') as f:
                
                
                f.seek(0) 
                f.truncate() 
                
                f.write(self.text_area.get('1.0', tk.END))
                f.close()
            
            self.text_area.delete(1.0, END)
            
        else:
            try:
                path = filedialog.asksaveasfile(filetypes = (("MD File", "*.md"),("All files", "*.*"))).name

            
            except:
                return   
            
            with open(path, 'w') as f:
                f.write(self.text_area.get('1.0', tk.END))
            

            dir = os.path.dirname(os.path.abspath(__file__))
            path = r"{0}\database_SL\\".format(dir)
            path=path.replace("\\","\\\\")
            dir_list=os.listdir(path)

            list_of_articles="𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝚁𝚃𝙸𝙲𝙻𝙴𝚂 <br> <br>"
            for x in dir_list:
                if x.endswith(".md"):
                    list_of_articles= list_of_articles + f"<a href='{path}\{x}'> {x[:-3]} </a><br>"

            self.left_label.set_html(list_of_articles)
    #function is binded with the event when the textbox for creating artciles is modified, basically for live rendering
    def inputEditorChange(self,event):
        self.text_area.edit_modified(0)
        markdownText = self.text_area.get("1.0", "end")
        html = reg(markdownText)
        self.Label_renderer.set_html(html)

    # function to display the contents of opened file in the editable textbox when edit button was pressed.
    def edit_file(self):
        self.edit=True
       
        if self.opened==True:
           
            stuff=self.controller.get_text(self.edit_this_var)
            self.text_area.delete(1.0, END)
            self.text_area.insert(1.0,stuff)


    # frames ###############################################################################################################

    def initializeFrames(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=26)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=18)
        self.columnconfigure(2,weight=6)
        
        
        self.top_frame=LabelFrame(self, bg="#F37878")
        self.top_frame.grid(row=0, column=0, columnspan=3,sticky = W, pady =2, padx=5)

        self.left_frame=LabelFrame(self, bg="black")
        self.left_frame.grid(row=1, column=0, rowspan=2,sticky = W, pady = 2)

        self.middle_frame=LabelFrame(self, bg="black")
        self.middle_frame.grid(row=1, column=1, rowspan=2, pady = 2)

        self.right_frame=LabelFrame(self, bg="black")
        self.right_frame.grid(row=1,column=2,sticky = E, pady = 2)

        self.right_frame.rowconfigure(0, weight=4)
        self.right_frame.rowconfigure(1, weight=1)


    # frames end ###########################################################################################################

    # menubar ##############################################################################################################

    def initialize_menu(self):
        mainmenu=Menu(self)
        mainmenu.add_command(label=" SAVE ", command=self.save_file_as)
        mainmenu.add_command(label=" EDIT ", command=self.edit_file)


        self.config(menu=mainmenu)
       
    #######################################################################################################################


    # initializing top frame################################################################################################

    def initialize_top_frame(self):
        img = Image.open("1.png")
        resize_img = img.resize((60 ,55))
        img = ImageTk.PhotoImage(resize_img)
        image_label=Label(self.top_frame,image=img)
        image_label.grid(row=0, column=0,sticky = W,padx=60, pady = 10)
        self.image_label=img
        heading=Label(self.top_frame, text="OUR - PEDIA", font="Algerian 34 ",  bg="#F37878", foreground="white")
        heading.grid(row=0, column=1,sticky = E, pady = 10, padx=500)
        

    ########################################################################################################################


    # populating right frame #############################################################################################

    def initialize_right_frame(self):
        self.text_area=scrolledtext.ScrolledText(self.right_frame,  wrap=tk.WORD ,bg="#F7ECDE", fg="black", font="arial 15", insertofftime=5, 
                                            insertontime=15, width="50")
        self.text_area.grid(row=0, column=0,sticky = W, pady = 2)
        self.text_area.bind("<<Modified>>", self.inputEditorChange)

        self.Label_renderer=HTMLScrolledText(self.right_frame, html="<p>Type Above to  <b>CREATE NEW</b></p>", background="#9ED2C6",
                                               foreground="white", state="disabled", width="68")
        self.Label_renderer.grid(row=1, column=0, pady = 2)


    #######################################################################################################################


    # populating middle frame #############################################################################################

    def initialize_middle_frame(self):

       # img1 = ImageTk.PhotoImage(Image.open("light.jpg"))
        self.Read_renderer=HTMLScrolledText(self.middle_frame, html="Here the selected article will appear",container=self, 
                                     background="#54BAB9", fg="white",state="disabled", width="70", height="44")
        self.Read_renderer.grid(sticky = W, pady = 4)

     #######################################################################################################################


    # Populating left frame.###############################################################################################

    def initialize_left_frame(self):

        self.left_topic=Label(self.left_frame,text="𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝚁𝚃𝙸𝙲𝙻𝙴𝚂",font="34", width=21, pady=10)
        self.left_topic.grid(row=0,column=0)
        self.left_label=HTMLScrolledText(self.left_frame, container=self, width="30", height="44", 
                                        background="#9ED2C6")

        
        
        dir = os.path.dirname(os.path.abspath(__file__))
        path = r"{0}\database_SL\\".format(dir)
        path=path.replace("\\","\\\\")
        list_of_articles=self.controller.getDirectory()
        setHTML = ""
        for x in list_of_articles:
                setHTML= setHTML + f"<a href='{path}\{x}.md'> {x} </a><br>"

        self.left_label.set_html(setHTML)
        self.left_label.configure(state='disabled')
        self.left_label.grid(row=1, column=0,sticky = W, pady = 2)

    def read_for_middle_frame(self,file_path):
        stuff = self.controller.get_html(file_path)
        if stuff!="":
            self.Read_renderer.set_html(stuff)
        else:
            self.Read_renderer.set_html("This article is <b>blank</b>, you can edit it though !!")