import os
import logging
def delete_excel(path):
    try:
        os.remove(path)
        logging.info(path+' deleted successfully')
    except FileNotFoundError:
        logging.error(path+' does not exist')

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path="newone2.xlsx"
delete_excel(path)
