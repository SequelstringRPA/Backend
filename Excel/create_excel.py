import os
import openpyxl
import logging
class FileExistError(Exception):
    pass

def create_excel(path,sheet_name):
    try:
        if os.path.isfile(path): 
            raise FileExistError
        wb = openpyxl.Workbook() 
        sheet = wb.active   
        sheet.title=sheet_name
        wb.save(path)
        logging.info(path+' Created Successfully')
    except FileExistError:
        #print(path+' already exists')
        logging.debug(path+' already exists')

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path=r'D:\Users\User\Desktop\Intern Project\Backend\Excel\newone.xlsx'
create_excel(path,sheet_name='Sheet 1')
