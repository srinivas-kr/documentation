import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)   #set the gpios to board mode
GPIO.setup(7,GPIO.OUT)     #set the gpio to output
def Blink(numTimes,speed):    #define a function to blink
    for i in range(0,numTimes):
        print "Iteration" +str(i+1)
        GPIO.output(7,True)
        time.sleep(speed)
        GPIO.output(7,False)
        time.sleep(speed)
    print "Done"
    GPIO.cleanup()            #cleanup the gpio.
iterations= raw_input("enter the total blinks")  
speed=raw_input(" enter the length of lbink in seconds")
Blink(int(iterations),float(speed))
