
    


#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep
GPIO.setmode(GPIO.BCM) ## Use board pin numbering

# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# now we'll define two threaded callback functions
# these will run in another thread when our events are detected

def my_callback2(channel):
    print "falling edge detected on 23"
    for i in range(0,5):  
            GPIO.output(24,True)
            sleep(0.5)## Wait
            GPIO.output(24,False)## Switch off pin 7
            sleep(0.5)## Wait


print "You will also need a third button connected so that when pressed"
print "it will connect GPIO port 17 (pin 11) to GND (pin 14)"
raw_input("Press Enter when ready\n>")


# when a falling edge is detected on port 23, regardless of whatever 
# else is happening in the program, the function my_callback2 will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)

try:
    print "Waiting for rising edge on port 24"
    GPIO.wait_for_edge(23, GPIO.RISING)  
    print "Rising edge detected on port 24. Here endeth the third lesson."

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
