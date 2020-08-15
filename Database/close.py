import mysql.connector
import logging

def close_connection(database,user,password):
    """ Connect to MySQL database """
    try:
        global conn;
        conn = mysql.connector.connect(host='localhost',database=database,
                                       user=user,password=password)
        conn.close() 
        logging.info('Connection to '+database+' database closed')
        #print('Connection closed')
    except mysql.connector.Error as e:
        logging.error("Error while closing connection")
        print(e)

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')  
database='test'
user='root'
password=''
close_connection(database,user,password)
