import logging
def read_file(path):
    try:
        file1 = open(path,"r")  
        print (file1.read())
        file1.close()
        logging.info(path+" read successfully")
    except FileNotFoundError:
        logging.error(path+" does not exist")

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
path = r'D:\Users\User\Desktop\Intern Project\Backend\Files\test.txt'
read_file(path)
