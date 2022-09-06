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
from model import Model
from view import View

class Controller():
    
    def __init__(self): 
        self.dir_list=[]
        self.model=Model() 
        self.view=View(self)


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

    def getDirectory(self):
        return self.model.fetchDirectory()
    
    def get_text(self,file_path):
        return self.model.fetch_text(file_path)

    def get_html(self,file_path):
        return self.model.generate_html(file_path)
Controller()