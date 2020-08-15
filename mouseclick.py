from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt",
                     level=logging.DEBUG,
                     format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved ")
    
def on_click(x, y, button, pressed):
    if pressed:
        logging.info("Mouse clicked")
    
def on_scroll(x, y, dx, dy):
    logging.info("Mouse scrolled ")

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()  
 
