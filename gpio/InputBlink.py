import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT) # And #24 as output to LED

# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
    for i in range(0,5):  
                GPIO.output(24,True)
                time.sleep(0.5)## Wait
                GPIO.output(24,False)## Switch off pin 7
                time.sleep(0.5)## Wait    

GPIO.output(24,False)

try:
        print (30 * '-')
        print ("   M A I N - M E N U")
        print (30 * '-')
        print ("1. On LED")
        print ("2. Off LED")
        print ("3. Blink")
        print (30 * '-')
         
        ## Get input ###
        choice = raw_input('Enter your choice [1-3] : ')
         
        ### Convert string to int type ##
        choice = int(choice)
         
        ### Take action as per selected menu-option ###
        if choice == 1:
                GPIO.output(24,True)
        elif choice == 2:
                GPIO.output(24,False)
        elif choice == 3:
                my_callback(24)
        else:    ## default ##
                print ("Invalid number. Try again...")

        time.sleep(1)
        GPIO.output(24,False)

                
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit 