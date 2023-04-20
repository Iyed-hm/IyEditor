from customtkinter import CTkTextbox, CTkScrollbar
from tkinter import Button

#! editor page
def text_editor_page_func(Frame, bar_name, name_of_tab, text_size, dict_of_path, text_box_content=''):
    """ this function of text editor """

    # Remove tab func
    def rm_tab():
        bar_name.delete(name_of_tab)
        del dict_of_path[name_of_tab]



    # Remove button
    rm_button = Button(Frame, text='x', fg='white', font=('', 7), bg='#FD5D5D', command=rm_tab)
    rm_button.place(x=1310, y=0)

    

    # Text Box
    text_area = CTkTextbox(Frame, width=1350, height=565, font=('', text_size), wrap='none')

    text_area.place(x=5, y=40)

    # Content of text box
    if text_box_content =='':
        pass
    else:
        text_area.insert('0.0', text_box_content)

    #* Save the content in dict 
    
    # dict of content
    text_area_content = {}
    # save the content of file in the dict
    text_area_content[name_of_tab] = text_box_content

    def update_text_dict(event):
        new_text = text_area.get('0.0', 'end')
        #text_area_content.update({name_of_tab : new_text})
        text_area_content[name_of_tab] = new_text
        #* printing dict for testing
        print(text_area_content)


        # Getting the dat file and update it
        #!#################


    text_area.bind("<KeyRelease>", update_text_dict)