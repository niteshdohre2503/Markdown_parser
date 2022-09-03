from tkinter import StringVar
import regex as re
import os

def new_reg(result, not_to_link):
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

    #ordered list
    regex_ol = r"(^(\s*)(\d+\.\s+)(.*))"
    subst_ol = "<p>\\1</p>"

    #linking while reading
    path=r'E:\\SL_Project_mywiki\\COP702_1\\database_SL\\'
    dir_list=os.listdir(path)
    
    for i in range(len(dir_list)):
        dir_list[i]=dir_list[i][:-3]
    
    for word in dir_list:
        if word!=not_to_link:
            regex_link = re.compile(word)
            result = regex_link.sub(r'<a href = "' + path + word + r'.md">' + word + r'</a>', result)
    ######################################################################################################
    result = re.sub(regex_h1, subst_h1, result, 0, re.MULTILINE)
    result = re.sub(regex_h2, subst_h2, result, 0, re.MULTILINE)
    result = re.sub(regex_h3, subst_h3, result, 0, re.MULTILINE)
    result = re.sub(regex_ib, subst_ib, result, 0, re.MULTILINE)
    result = re.sub(regex_b, subst_b, result, 0, re.MULTILINE)
    result = re.sub(regex_i, subst_i, result, 0, re.MULTILINE)
    result = re.sub(regex_ol, subst_ol, result, 0, re.MULTILINE)

    
    return result

