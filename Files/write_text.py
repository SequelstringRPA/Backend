import logging
def write_file(path,data):
    file1 = open(path,"a") 
      
    file1.write(data)
    file1.close()
    logging.info("Successfully written in "+path)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
data = "data to be written \n"
path = r'D:\Users\User\Desktop\Intern Project\Backend\Files\test.txt'
write_file(path,data)
