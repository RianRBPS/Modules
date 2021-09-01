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