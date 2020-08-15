import logging
import csv
def write_csv(path,data):
    with open(path, mode='a') as file:
        writer = csv.writer(file, lineterminator = '\r')
        writer.writerow(data)
    logging.info('Successfully written in '+path)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
data=['Data', 'to', 'be', 'written']
path = r'D:\Users\User\Desktop\Intern Project\Backend\Files\data.csv'
write_csv(path,data)       
