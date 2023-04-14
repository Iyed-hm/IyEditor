#! //----------\\Modules//----------\\


from customtkinter import set_appearance_mode, set_default_color_theme, CTk, CTkFrame, CTkTabview, CTkButton, CTkLabel
from tkinter import Menu, PhotoImage
from packages.pages.welcome_page import *
from packages.pages.text_editor import *



#! //----------\\Screen//----------\\


#* Theme settings
appearance_mode = 'light'
default_color_theme = 'blue'

#* Theme
set_appearance_mode(appearance_mode) 
set_default_color_theme(default_color_theme)

#* Window
root = CTk()

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# set the size of the window to match the screen
root.geometry(f"{screen_width}x{screen_height}")
# min width and min height
root.minsize(width=1050, height=550)

#* Window title
root.title('IyEditor')



#! //----------\\Functions//----------\\


#* Help functions
def welcome():
    try:
        wksFlatBar.add('Welcome')
        welcome_page_func(wksFlatBar.tab('Welcome'), wksFlatBar, new_file_cmd=new_file)
    except:
        wksFlatBar.set('Welcome')


def new_file():
    nb = 1
    name_of_file = f"Untitled-{nb}"
    try:
        wksFlatBar.add(name_of_file)
        text_editor_page_func(wksFlatBar.tab(name_of_file), wksFlatBar, name_of_file, text_size=editor_text_size)
        wksFlatBar.set(name_of_file)
    except:
        while True:
            try:
                nb += 1
                name_of_file = f"Untitled-{nb}"
                wksFlatBar.add(name_of_file)
                text_editor_page_func(wksFlatBar.tab(name_of_file), wksFlatBar, name_of_file, text_size=editor_text_size)
                wksFlatBar.set(name_of_file)
                break
            except:
                continue
                


#! //----------\\Editor Settings//----------\\


# text size
editor_text_size = 18



#! //----------\\Flat Bar//----------\\


#* Flat Bar
flatBar = Menu(root)

#* File
file = Menu(flatBar, tearoff=False)

#* Edit
edit = Menu(flatBar, tearoff=False)

#* Help
help = Menu(flatBar, tearoff=False)

#* Centent of file and her image
img_new_file = PhotoImage(file="img/File/new_file.png")
file.add_command(label=' New File', image=img_new_file, compound='left', command=new_file)
img_open_file = PhotoImage(file="img/File/open_file.png")
file.add_command(label=' Open File', image=img_open_file, compound='left')
file.add_separator()
img_save = PhotoImage(file="img/File/save.png")
file.add_command(label=' Save', image=img_save, compound='left')
img_save_as = PhotoImage(file="img/File/save_as.png")
file.add_command(label=' Save As', image=img_save_as, compound='left')
file.add_separator()
img_exit = PhotoImage(file="img/File/exit.png")
file.add_command(label=' Exit', command=root.quit, image=img_exit, compound='left')

#* Centent of edit
img_cut = PhotoImage(file="img/Edit/cut.png")
edit.add_command(label=' Cut', image=img_cut, compound='left')
img_copy = PhotoImage(file="img/Edit/copy.png")
edit.add_command(label=' Copy', image=img_copy, compound='left')
img_past = PhotoImage(file="img/Edit/paste.png")
edit.add_command(label=' Paste', image=img_past, compound='left')
edit.add_separator()
img_select_all = PhotoImage(file="img/Edit/select_all.png")
edit.add_command(label=' Select All', image=img_select_all, compound='left')

#* Centent of help
img_welcome = PhotoImage(file="img/Help/welcome.png")
help.add_command(label=' Welcome', image=img_welcome, compound='left', command=welcome)
help.add_separator()
img_settings = PhotoImage(file="img/Help/settings.png")
help.add_command(label=' Settings', image=img_settings, compound='left')
help.add_separator()
img_about = PhotoImage(file="img/Help/about.png")
help.add_command(label=' About', image=img_about, compound='left')

#* Set buttons
flatBar.add_cascade(label='File', menu=file)
flatBar.add_cascade(label='Edit', menu=edit)
flatBar.add_cascade(label='Help', menu=help)

#* set flatBar
root.config(menu=flatBar)



#! //-------------\\ Workspace //-------------\\


#* Frame of workspace
wks = CTkFrame(root, height=screen_height, width=screen_width)
wks.place(x=0, y=0)

#* wksFlatBar
wksFlatBar = CTkTabview(wks, height=screen_height, width=screen_width)
wksFlatBar.pack()
wksFlatBar.add('Welcome')


#* Welcome page
welcome_page_func(wksFlatBar.tab('Welcome'), wksFlatBar, new_file_cmd=new_file)

# text editor page
"""#! test !#
wksFlatBar.add('test')
text_editor_page_func(wksFlatBar.tab('test'), wksFlatBar, 'test', text_size=editor_text_size)"""



#! //-------------\\ End //-------------\\
root.mainloop()
