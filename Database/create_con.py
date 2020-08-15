import mysql.connector
import logging

def connect(database,user,password):
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',database=database,
                                       user=user,password=password)
        if conn.is_connected():
            logging.info('Connected to '+database+' database')
            #print('Connected to MySQL database')

    except mysql.connector.Error as e:
        logging.error('Error while connecting to database')
        #print(e)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')  
database='test'
user='root'
password=''
connect(database,user,password)
