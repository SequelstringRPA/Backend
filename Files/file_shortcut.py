import os, winshell
from win32com.client import Dispatch
import logging

def createShortcut(target,name):    
    desktop = winshell.desktop()
    path=os.path.join(desktop,name+'.lnk')
    wDir=os.path.dirname(target)
    icon=''
    try:
        if not os.path.exists(target):
            raise FileNotFoundError
        filename=''
        i=2
        while os.path.exists(path):
            filename=name+'('+str(i)+')'
            path=os.path.join(desktop,filename+'.lnk')
            i+=1
            print('Same name file exists\nCreating %s'%filename)
            logging.info('Same name file exists\nCreating %s'%filename)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        if icon == '':
            pass
        else:
            shortcut.IconLocation = icon
        shortcut.save()
        logging.info('Shortcut of %s created at %s'%(target,path))

    except FileNotFoundError:
        print('File not found')
        logging.error('%s file not found'%target)
        
logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', 
                    level=logging.DEBUG, filemode='a') 
target=r'D:\Users\User\Desktop\Intern Project\Backend\temp\test'
name='first'
createShortcut(target,name)
