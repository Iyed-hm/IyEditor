from customtkinter import CTkTextbox, CTkScrollbar
from tkinter import Button


def text_editor_page_func(Frame, bar_name, name_of_tab, text_size):
    """ this function of text editor """

    # Remove tab func
    def rm_tab():
        bar_name.delete(name_of_tab)


    # Remove button
    rm_button = Button(Frame, text='x', fg='white', font=('', 7), bg='#FD5D5D', command=rm_tab)
    rm_button.place(x=1310, y=0)

    # Text Box
    text_area = CTkTextbox(Frame, width=1350, height=565, font=('', text_size))
    text_area.place(x=5, y=40)


