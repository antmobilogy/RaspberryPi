#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

def main():

    # tell the GPIO module that we want to use the 
    # chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # setup pin 25 as an output
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)
    
    GPIO.output(24,False)
    i=0
    while True:
        if GPIO.input(23):
             # the button isn't being pressed, so the LED off 
             # and turn off the red LED
             GPIO.output(24,False)
             print i , ": button not pressed, LED off"
             i = i + 1
        else:
             # the button is being pressed, so turn on the LED
             # and turn on the red LED
             GPIO.output(24,True)
             print i , ": button pressed, LED on"
             i = i + 1
        time.sleep(0.1)
 
    GPIO.cleanup()



if __name__=="__main__":
    main()

        
