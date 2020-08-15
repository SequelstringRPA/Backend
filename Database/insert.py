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

def insert(tablename,values):
    cursor = conn.cursor()
    try:
        sql = "insert into "+tablename+" values(%s, %s)"
        cursor.execute(sql,values)
        conn.commit()
        #print(cursor.rowcount, "record inserted.")
        logging.info("%d record(s) inserted." %cursor.rowcount)
    except mysql.connector.ProgrammingError as e:
        #print(e)
        logging.error(e)
    except mysql.connector.Error as e:
        #print(e)
        logging.error(e)

tablename="customers"
values=["xyz",'456 pqr']
if con:
    insert(tablename,values)

