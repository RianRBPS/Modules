# pwd -> Where I am

n = int(input('_'))
if n == 2:
    f = open('practice.txt','w+')
    f.write('This is a test string')
    f.close()
else:
    print('Arquivo não criado')

###################################################

import os

print(os.getcwd()) # Currently Working Directory
print(os.listdir()) # All items in cwd
print(os.listdir('C:\\Users')) # All items in this directory

###################################################

import shutil

shutil.move(src='practice.txt',dst='C:\\Users\kingt\OneDrive\Desktop')

os.listdir('C:\\Users\kingt\OneDrive\Desktop')

##################################################

'''Deleting Files
NOTE: The os module provides 3 methods for deleting files:

    os.unlink(path) which deletes a file at the path your provide
    os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
    shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
Instead we will use the send2trash module.
A safer alternative that sends deleted files to the trash bin instead of permanent removal.*'''