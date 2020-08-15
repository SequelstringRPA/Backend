import logging
import shutil
import os, re, os.path
def delete_temp(path):
    shutil.rmtree(path)
    logging.info(path+" deleted successfully")

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path = r"D:\Users\User\Desktop\Intern Project\Backend\Files\test"
delete_temp(path)
