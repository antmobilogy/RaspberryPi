import RPi.GPIO as GPIO ## Import GPIO library
import time
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(23, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(23,False)## Switch off pin 7
    

print "Done" ## When loop is complete, print "Done"
GPIO.cleanup()