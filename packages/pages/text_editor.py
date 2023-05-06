from customtkinter import CTkTextbox, CTkScrollbar
from tkinter import Button
from pickle import dump, load

#! editor page
def text_editor_page_func(Frame, bar_name, name_of_tab, text_size, dict_of_path, text_box_content=''):
    """ this function of text editor """

    # Remove tab func
    def rm_tab():
        # Delete the path of page from pict_of_path
        del dict_of_path[name_of_tab]
        # Delete the  page from dict of pages area
        # Get the dict of pages area
        with open('.IyEditor_cache_/IyEditor.dat', 'rb') as dat_file_r:
            dict_of_pages_area = load(dat_file_r)
        # deleting and dumping the dict to the dat file
        with open('.IyEditor_cache_/IyEditor.dat', 'wb') as dat_file_w:
            # delete
            del dict_of_pages_area[name_of_tab]
            # dump
            dump(dict_of_pages_area, dat_file_w)
        # Delete the page
        bar_name.delete(name_of_tab)



    # Remove button
    rm_button = Button(Frame, text='x', fg='white', font=('', 7), bg='#FD5D5D', command=rm_tab)
    rm_button.place(x=1310, y=0)

    

    # Text Box
    text_area = CTkTextbox(Frame, width=1350, height=565, font=('', text_size), wrap='none')

    text_area.place(x=5, y=40)



    def update_text_dict(event):
        # Get the Content of text area
        new_text = text_area.get('0.0', 'end')
        # Get the dict of pages area
        with open('.IyEditor_cache_/IyEditor.dat', 'rb') as dat_file_r:
            dict_of_pages_area = load(dat_file_r)
        # update and dumping the dict to the dat file
        with open(r'.IyEditor_cache_/IyEditor.dat', 'wb') as dat_file_w:
            # update
            dict_of_pages_area[name_of_tab] = new_text
            # dump
            dump(dict_of_pages_area, dat_file_w)


    # Content of text box
    if text_box_content =='':
        pass
    else:
        text_area.insert('0.0', text_box_content)
        update_text_dict()


        # test func
        """with open('../../', 'rb') as bin_files:
            content = load(bin_files)
            print(content)"""


    text_area.bind("<KeyRelease>", update_text_dict)