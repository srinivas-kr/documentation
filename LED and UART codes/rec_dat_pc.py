
#this code recives data from PC to be store data on Pi
import serial
import sqlite3
import RPi.GPIO as GPIO
import time

def get_temp_val():
    ser=serial.Serial('/dev/ttyAMA0',9600)
    ser.open()
    while True:
        temp=ser.read(ser.inWaiting())
        print temp
        conn=sqlite3.connect('tempsensor.db')
        c=conn.cursor()
        c.execute("""INSERT INTO sensor values(date('now'),time('now'),(?))""",(temp,))
        conn.commit()
        t=20
        for row in c.execute('SELECT *FROM sensor WHERE temp>(?)',(t,)):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7,GPIO.OUT)
            GPIO.output(7,True)
            time.sleep(1)
            GPIO.output(7,False)
            time.sleep(1)
        GPIO.cleanup()
get_temp_val()
