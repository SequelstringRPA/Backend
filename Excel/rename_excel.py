import os
import logging
def rename_excel(source,dest):
        try : 
                os.rename(source, dest) 
                logging.info(source+' successfully renamed to '+dest)

        # For permission related errors 
        except PermissionError:
                logging.error('Permission Denied')

        # For other errors 
        except OSError as error: 
                logging.error(error) 

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
source = r'D:\Users\User\Desktop\Intern Project\Backend\Excel\newone2.xlsx'
dest = r'D:\Users\User\Desktop\Intern Project\Backend\Excel\newone2.xlsx'
rename_excel(source,dest)
