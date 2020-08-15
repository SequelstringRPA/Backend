import zipfile
from zipfile import ZipFile 
import os
import logging
def unzip_files(filepath,extract_path,password):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError
        with ZipFile(filepath, 'r') as zip: 
            # printing all the contents of the zip file 
            zip.printdir() 

            # extracting all the files 
            print('Extracting all the files now...') 
            zip.extractall(extract_path, pwd = bytes(password, 'utf-8')) 
            print('Done!')
            logging.info("%s file extracted to %s"%(filepath,extract_path))

    except FileNotFoundError:
        print("File does not exists")
        logging.error("%s file not found"%filepath)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')
filepath = r"D:\Users\User\Desktop\Intern Project\Backend\temp\testpass.zip"
extract_path = r"D:\Users\User\Desktop\Intern Project\Backend\temp"
password='one'
unzip_files(filepath,extract_path,password)
