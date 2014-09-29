# Notifier example from tutorial
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pigpio
pi1 = pigpio.pi()
import pyinotify, shutil
#import RPi.GPIO as GPIO
wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CREATE  # watched events
des = '/home/pi/Downloads/used'

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname
	print "opening file"
	f = open(event.pathname, 'r')
    	for line in f:
            print line
            if line == "start\n":
		print "start working ....."
                #GPIO.output(11, GPIO.HIGH)
                pi1.write(4, 1)
            elif line == "stop\n":
		print "stop working ....."
                #GPIO.output(11, GPIO.LOW)
		pi1.write(4, 0)
	print "moving file"
        shutil.move(event.pathname, des)
	print "moving done"	

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/pi/Downloads', mask)

notifier.loop()
