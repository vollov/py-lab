# -*- coding: utf-8 -*-
import os, sys

'''Utility tools to update file names under a directory'''

def removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)

def move(directory, sub_str_to_replace, sub_str):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory_to_update = ur""+os.path.join(current_directory, directory)
    os.chdir(directory_to_update)
    for file_name in os.listdir(directory_to_update):
        new_file_name = removeNonAscii(file_name)
        new_file_name = new_file_name.replace(sub_str_to_replace,sub_str)
        if new_file_name != file_name:
            if os.path.isfile(new_file_name):
                print new_file_name + ' is existing, skipping change file name'
            else:
                os.rename(file_name, new_file_name)
        
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage:'
        print 'python rm.py dir_name key_to_replace string'
        sys.exit()
        
    directory = sys.argv[1]
    sub_str_to_replace = sys.argv[2]
    sub_str = sys.argv[3]
    move(directory, sub_str_to_replace, sub_str)