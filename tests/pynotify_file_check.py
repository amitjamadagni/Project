import pyinotify
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE
class EventHandler(pyinotify.ProcessEvent):
	def process_IN_CREATE(self, event):
		print "Creating", event.pathname
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/pi/Downloads',mask)
notifier.loop()
