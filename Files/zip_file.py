# importing required modules 
from zipfile import ZipFile 
import os 
import logging

flag=False
def get_all_file_paths(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError

    # initializing empty file paths list 
        filepaths = []
        global flag

        # crawling through directory and subdirectories 
        for root, directories, files in os.walk(directory): 
            for filename in files: 
                # join the two strings in order to form the full filepath. 
                filepath = os.path.join(root, filename) 
                filepaths.append(filepath) 
        return filepaths		 


    except FileNotFoundError:
        logging.error("%s folder not found"%directory)
        print("File not found")
        flag=True

def zip_file(directory,file_paths,zip_path):
    try:
        # printing the list of all files to be zipped 
        print('Following files will be zipped:') 
        for file_name in file_paths: 
            print(file_name)
        if not os.path.exists(zip_path):
            raise FileNotFoundError

        # writing files to a zipfile 
        with ZipFile(zip_path,'w') as zip: 
            # writing each file one by one 
            for file in file_paths: 
                zip.write(file) 

        print('All files zipped successfully!')
        logging.info('%s zipped successfully to %s'%(directory,zip_path))

    except FileNotFoundError:
        print("File not found")
        logging.error("%s file not found"%zip_path)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')
directory = r"D:\Users\User\Desktop\Intern Project\Backend\temp\test"
file_paths = get_all_file_paths(directory)
print(flag)
zip_path = r"D:\Users\User\Desktop\Intern Project\Backend\temp\test.zip"
if flag==False:
    zip_file(directory,file_paths,zip_path)
