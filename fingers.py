
import threading
from time import sleep

xVal = 0
yVal = 0

def listen():
	import trackpad
	print "listening"
	trackpad.listen()
	n = 0
	while n < 1:
		print "while"
		print trackpad.currentX
		print trackpad.currentY
		sleep(0.5)
	