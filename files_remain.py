'''
#directory file to read
dir=input('Enter directory file to read: ')

f = open(dir, "r")

#read content of file
print(f.read())

'''

#multiple files part
import os
folder_path = 'C:/Users/Akshada/Desktop/RPA_backend'

def listdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print('FileName is: ' +filename)
        print('Folder Path: '+os.path.abspath(os.path.join(dir,filename)),sep='\n')

if __name__ == '__main__':
    listdir(folder_path)
