import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(24, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    
for i in range(0,5):  
            GPIO.output(24,True)
            sleep(0.5)## Wait
            GPIO.output(24,False)## Switch off pin 7
            sleep(0.5)## Wait


print "Done" ## When loop is complete, print "Done"
GPIO.cleanup()