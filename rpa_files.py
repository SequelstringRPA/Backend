#files part
import os
import shutil
import logging

logging.basicConfig(filename="logfile.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')
#create object
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
'''
#files rename and remove

src=input("Enter file name:")
dest=input("Enter new name:")
os.rename(src,dest)
#os.remove(src)
logger.info("Renamed successfully")
#logger.info("Removed successfully")
'''
'''
#move file

src = 'C:/Users/Akshada/Desktop/RPA_backend/files_sample/first.txt'
dest = 'C:/Users/Akshada/Desktop/RPA_backend/first.txt'

file=shutil.move(src,dest)
 
logger.info("moved successfully") 
'''
'''
#copy file

src = 'C:/Users/Akshada/Desktop/RPA_backend/first.txt'
dest = 'C:/Users/Akshada/Desktop/RPA_backend/files_sample'

file=shutil.copy(src,dest)  
logger.info("File copied")
'''
'''
#create file
path = input('Enter path of directory: ')
src=input('Enter source of file: ')
file=input('Enter filename: ')

with open(os.path.join(path,src,file),'w') as fp:
    pass
logger.info('File created')

#files part ends
'''

#folder part
'''
#create folder
file=input('Enter file to be created: ')
parent_dir=input('Enter directory: ')

path=os.path.join(parent_dir,file)
os.mkdir(path)
logger.info('Folder created')
'''
'''
#delete folder

file=input('Enter file to be deleted: ')
parent_dir=input('Enter directory where present: ')

path=os.path.join(parent_dir,file)

os.rmdir(path)
logger.info("Directory '% s' deleted" % file)
'''
'''
#rename folder
src=input('Enter file to be renamed: ')
src_dir=input('Enter directory where present: ')
path=os.path.join(src_dir,src)
dest=input('Enter newname of file: ')

os.rename(path,dest)
logger.info('Successfully done')
'''
'''
#move folder
src = 'C:/Users/Akshada/Desktop/RPA_backend/new_renamed'
dest = 'C:/Users/Akshada/Desktop/RPA_backend/folder_sample'

file=shutil.move(src,dest)
 
logger.info("moved folder successfully")
'''
'''
#copy folder
def copy_excel(source,destination):
        try: 
                dest=shutil.copytree(source, destination) 
                logger.info("Folder copied successfully.") 

        # If there is any permission issue 
        except PermissionError: 
                logger.info("Permission denied.") 

        #if file is already present
        except FileExistsError:
                logger.info("Folder already exists")

        # For other errors 
        except: 
                logger.info("Error occurred while copying file.") 

source = 'C:/Users/Akshada/Desktop/RPA_backend/files_sample'
destination = 'C:/Users/Akshada/Desktop/RPA_backend/folder_sample/files_sample'
copy_excel(source,destination)

'''

