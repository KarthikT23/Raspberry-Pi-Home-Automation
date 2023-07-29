from pushbullet import Pushbullet
from time import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,False)
GPIO.setup(40,GPIO.OUT)
pb = Pushbullet(“o.BhDxXePii01lpQg3re2dJEws7UnRhcEx”)
print(pb.devices)
while True:
	i=GPIO.input(11)
	j=GPIO.input(13)
	k=GPIO.input(40)
	if i==0 and j==0:
		print(“No motion detected”)
		sleep(10)
	elif i==1 and j==0:
		print(“Person at the door”)
		dev=pb.get_device(“Motorola Moto g(9)”)
		push=dev.push_note(“Alert!”, ”Someone is at the door!”)
		if k==False:
			print(“ambient light is present”)
			GPIO.output(40,False)
		elif k==True:
			print(“ambient light is not present”)
			dev=pb.get_device(“Motorola Moto g(9)”)
			push=dev.push_note(“Alert!”, ”Not enough ambient light, lights will be switched on”)
        sleep(10)
	elif i==0 and j==1:
		print(“Person is inside the house”)
		dev=pb.get_device(“Motorola Moto g(9)”)
		push=dev.push_note(“Alert!”, ”Someone is in the house!”)
		if k==False:
			print(“ambient light is present”)
			GPIO.output(40,False)
		elif k==True:
			print(“ambient light is not present”)
			dev=pb.get_device(“Motorola Moto g(9)”)
			push=dev.push_note(“Alert!”, ”Not enough ambient light, lights will be switched on”)
		sleep(10)
	elif i==1 and j==1:
		print(“Person is wandering around the house”)
		dev=pb.get_device(“Motorola Moto g(9)”)
		push=dev.push_note(“Alert!”, ”Someone is wandering around the house!”)
		if k==False:
			print(“ambient light is present”)
			GPIO.output(40,False)
		elif k==True:
			print(“ambient light is not present”)
			dev=pb.get_device(“Motorola Moto g(9)”)
            push=dev.push_note(“Alert!”, ”Not enough ambient light, lights will be switched on”)
		sleep(10)
