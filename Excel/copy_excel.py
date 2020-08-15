import shutil
import logging
def copy_excel(source,destination):
        try: 
                shutil.copyfile(source, destination) 
                logging.info(source+' successfully copied to '+destination)
        # If source and destination are same 
        except shutil.SameFileError: 
                logging.error(source+' and '+destination+' represents the same file.')

        # If there is any permission issue 
        except PermissionError: 
                 logging.error('Permission Denied')
        # For other errors 
        except: 
                logging.error("Error occurred while copying file.") 

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
source = r"D:\Users\User\Desktop\Intern Project\Backend\Excel\newone2.xlsx"
destination = r"D:\Users\User\Desktop\Intern Project\Backend\newone2.xlsx"
copy_excel(source,destination)
