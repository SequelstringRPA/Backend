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
        #print("Connection error")
    return flag

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')  
database='test'
user='root'
password=''
con=connect(database,user,password)

def delete(tablename,values,where):
    cursor = conn.cursor()
    try:
        sql = "delete from "+tablename+" where "+where+"=%s"
        cursor.execute(sql,values)
        conn.commit()
        #print(cursor.rowcount, "record deleted.")
        logging.info("%d record(s) deleted." %cursor.rowcount)
    except mysql.connector.ProgrammingError as e:
        #print("Programming error")
        logging.error(e)
    except mysql.connector.Error as e:
        #print(e)
        logging.error(e)
        
tablename="customers"
values=['xyz']
where="name"
if con:
    delete(tablename,values,where)

