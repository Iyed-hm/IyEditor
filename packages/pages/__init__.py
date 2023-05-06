""" Create the dat file of pages data """


# Import mkdir and path from os
from os import mkdir, path
# Import dump from pickle module 
from  pickle import dump


# Check if the folder is exist
check = path.isdir('.IyEditor_cache_')

# Check == False
if not check:
    # Create the Folder of dat_file
    mkdir('.IyEditor_cache_/')

    # Create the dit of pages data
    dat = {}

    # Create dat file
    with open('.IyEditor_cache_/IyEditor.dat', 'wb') as dat_file:
        # Adding the dict to dat file
        dump(dat, dat_file)