from random import randint
import os
input_ = raw_input("Enter the action to be performed\n")
if input_ == "start":
    x = str(randint(00000,99999))
    new_file = open("/home/pi/Downloads/"+x+".txt","w")	
    os.chmod("/home/pi/Downloads/"+x+".txt", 0755)
    new_file.write("start\n")
elif input_ == "stop":
    x = str(randint(00000,99999))
    new_file = open("/home/pi/Downloads/"+x+".txt","w")
    new_file.write("stop\n")
    os.chmod("/home/pi/Downloads/"+x+".txt", 0755)
else: 
    print "Check the input"

