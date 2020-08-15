import logging
import csv
def read_csv(path):
    try:
        with open(path,'r')as f:
          data = csv.reader(f)
          for row in data:
              print(row)
        logging.info(path+' read successfully')      
    except FileNotFoundError:
        logging.error(path+' does not exists')

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path = r'D:\Users\User\Desktop\Intern Project\Backend\Files\data.csv'
read_csv(path)       
