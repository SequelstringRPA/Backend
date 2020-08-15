import os
import logging
class FolderNotFoundError(Exception):
    pass

def delete_part_file(directory):
        del_files=[]
        for f in os.listdir(directory):
            if f.endswith('.part'):
                del_files.append(f)
        return del_files

logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
directory=r'D:/Users/User/Desktop/Intern Project/Backend/Files'
try:
    if not os.path.exists(directory): 
        raise FolderNotFoundError
    del_files=delete_part_file(directory)
    if del_files == []:
        logging.error('No part files in '+directory)
    else:
        for f in del_files:
            os.remove(os.path.join(directory,f))
            logging.info('Part files successfully deleted in '+directory)

except FolderNotFoundError:
    logging.error(directory+' does not exists')
    
