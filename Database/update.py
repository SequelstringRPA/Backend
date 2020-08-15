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

def update(tablename,values,sett,where):
    cursor = conn.cursor()
    try:
        sql = "update "+tablename+" set "+sett+"=%s where "+where+"=%s"
        cursor.execute(sql,values)
        conn.commit()
        #print(cursor.rowcount, "record updated.")
        logging.info("%d record(s) updated." %cursor.rowcount)        
    except mysql.connector.ProgrammingError as e:
        #print("Programming error")
        logging.error(e)
    except mysql.connector.Error as e:
        #print(e)
        logging.error(e)

tablename="customers"
values=['123 xyz','xyz']
sett="address"
where="name"
if con:
    update(tablename,values,sett,where)

