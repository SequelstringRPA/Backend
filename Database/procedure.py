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
        #print("connection error")

    return flag

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a')  
database='test'
user='root'
password=''
con=connect(database,user,password)

def call_procedure(proc_name,args):
    try:
        cursor = conn.cursor()
        
        cursor.callproc(proc_name,args)
        result_args = cursor.callproc(proc_name,args)
        logging.info(result_args)
        #print("result arg:",result_args)
        
        # print out the result
        for x in cursor.stored_results():
            result=[]
            result.append(x.fetchall())
            #print("result",result)
            logging.info(result)            
 
    except mysql.connector.ProgrammingError as e:
        #print(e)
        logging.error(e)

if con:
    call_procedure(proc_name='find_both', args=[1,0])












