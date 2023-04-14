# modules
from customtkinter import CTkLabel, CTkButton
from tkinter import Button

# welcome page func
def welcome_page_func(Frame, bar_name, new_file_cmd):
    """ this function to add the welcome page of IyEditor """

    # Remove tab func
    def rm_tab():
        bar_name.delete('Welcome')


    # Remove button
    rm_button = Button(Frame, text='x', fg='white', font=('', 7), bg='#FD5D5D', command=rm_tab)
    rm_button.place(x=1310, y=0)

    # Label Start
    CTkLabel(Frame, text='Start :', font=('', 30)).place(x=150, y=110)

    # Buttons newFile and openFile
    btn_new_file = CTkButton(Frame, text='New File', width=50, height=35, command=new_file_cmd)
    btn_new_file.place(x=220, y=160)
    btn_open_file = CTkButton(Frame, text='Open File', width=50, height=35)
    btn_open_file.place(x=220, y=200)

    # logo
    CTkLabel(Frame, text='Iy', font=('courier', 120), text_color='#EA5455').place(x=560, y=250)
    CTkLabel(Frame, text='Editor', font=('courier', 120), text_color='#002B5B').place(x=700, y=250)

    # Dev label
    CTkLabel(Frame, text='Developed By Iyed @2023').place(x=1200, y=590)