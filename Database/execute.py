import mysql.connector
import logging

def connect(database,user,password):
    """ Connect to MySQL database """
    try:
        flag=False
        global conn;
        conn = mysql.connector.connect(host='localhost',database=database,
                                       user=user,password=password)
        if conn.is_connected():
            logging.info('Connected to '+database+' database')
            #print('Connected to MySQL database')
            flag=conn.is_connected()
 
    except mysql.connector.Error as e:
        logging.error('Error while connecting to '+database+' database')
        #print(e)
    return flag

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')  
database='test'
user='root'
password=''
con=connect(database,user,password)

def execute(sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            #print(x)
            logging.info(x)

    except mysql.connector.ProgrammingError as e:
        #print(e)
        logging.error(e)

sql = "select * from customers"
if con:   
    execute(sql)
