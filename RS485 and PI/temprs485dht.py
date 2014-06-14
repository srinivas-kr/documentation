import serial
import sqlite3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
conn=sqlite3.connect('temp_table.db')
c=conn.cursor()
def get_temp_val():
    ser=serial.Serial('/dev/ttyAMA0',9600,timeout=1)
    ser.close()
    ser.open()
    try:
        while True:
            GPIO.output(7,1) 
            time.sleep(.5)
            val=raw_input("enter something:") #send some value to ARDUINO
            ser.write(val)
            time.sleep(.5)
            GPIO.output(7,0) 
            time.sleep(5)
            temp=ser.read(ser.inWaiting())
            print "received temp is :", temp
            #c.execute("""INSERT INTO sensor values(date('now'),time('now'),(?))""",(temp,))
            #conn.commit()
            #t=30
            #for row in c.execute('SELECT *FROM sensor WHERE temp>(?)',(t,)):
                #GPIO.output(12,True)
                #time.sleep(.2)
                #GPIO.output(12,False)
                #time.sleep(.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
get_temp_val()
