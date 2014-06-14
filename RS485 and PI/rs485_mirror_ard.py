import serial
import sqlite3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)# GPIO set out for blinking LED
#GPIO.setup(12,GPIO.OUT) # GPIO setting for muxing receive/transmit mode on MAX485.
conn=sqlite3.connect('tempsensor.db') #connect to database
c=conn.cursor() #connect to database
def get_temp_val(): # function for getting some value.
    ser=serial.Serial('/dev/ttyAMA0',9600) #enable the serial port
    ser.close()
    ser.open() 
    while True:   #loop for reapeated actions.
        GPIO.setup(7,1) #enable  transmit mode on MAX485
        #print "i am high"
        time.sleep(4)
        val=raw_input("enter something:") #send some value to ARDUINO
        ser.write(val)
        
        #time.sleep(.5)
        GPIO.setup(7,0) #switch the MAX485 to receive mode.
        #print "i am low"
        time.sleep(4)
        temp=ser.read(ser.inWaiting())
        print "received data is", temp 
        #c.execute("""INSERT INTO sensor values(date('now'),time('now'),(?))""",(temp,))
        #conn.commit()
        GPIO.cleanup()
        t=20
        #for row in c.execute('SELECT *FROM sensor WHERE temp>(?)',(t,)):
            #GPIO.output(7,True)
            #time.sleep(.2)
            #GPIO.output(7,False)
            #time.sleep(.2)
        #GPIO.cleanup()
get_temp_val()


