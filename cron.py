import glob
import shutil
import RPi.GPIO as GPIO
import time

start = 0
stop = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
src = '/home/pi/Downloads/*.txt'
des = '/home/pi/Downloads/used/'
files = glob.glob(src)
for file in files:
    f = open(file, 'r')
    for line in f:
	if line == "start\n":	
	   GPIO.output(12, GPIO.HIGH)	
	elif line == "stop\n":
	   GPIO.output(12, GPIO.LOW)
	else:
	    print "Invalid input"
    shutil.move(file, des)
