import pyinotify
import glob
import shutil
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE
class EventHandler(pyinotify.ProcessEvent):
	def __init__(self, pin):
		self.pin = pin

	def process_IN_CREATE(self, event):
		GPIO.setup(self.pin, GPIO.OUT)
		print event.pathname
		act = self._rlines(event.pathname)
		print act[0]
		if act[0] == "start":
			print "Checking if the activity is already up"
			if GPIO.input(self.pin) == 1:
				print "Already turned on"
				self._mov_file(event.pathname)
			else:
				GPIO.output(self.pin, True)
				print "Starting the activity"
				self._mov_file(event.pathname)
		elif act[0] == "stop":
			print "Checking if the activity is already down"
			if GPIO.input(self.pin) == 0:
				print "Already turned off"
				self._mov_file(event.pathname)
			else:
				GPIO.output(self.pin, False)
				print "Stopping the activity"
				self._mov_file(event.pathname)
	
	def _rlines(self, filename): 
		f = open(filename)
		file = [line.strip() for line in f]
		f.close
		return file
	         
	def _mov_file(self, filename):
		des = '/home/pi/Downloads/used/'
		shutil.move(filename, des)
				 
handler = EventHandler(12)
notifier = pyinotify.Notifier(wm, handler.process_IN_CREATE)
wdd = wm.add_watch('/home/pi/Downloads',mask)
notifier.loop()

