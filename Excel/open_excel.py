import os
from win32com.client import Dispatch
import logging
class FileNotExistError(Exception):
    pass

def open_excel(path):
    try:
        if not os.path.isfile(path): 
            raise FileNotExistError        
        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(path)
        logging.info(path+' opened successfully')
    except FileNotExistError as e:
            logging.info(path+' does not exist')

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path=r'D:\Users\User\Desktop\Intern Project\Backend\Excel\newone2.xlsx'
open_excel(path)
