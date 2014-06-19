##send quirey to arduino over xbee modules to receive temperature and humidity
 #with repeater 
import serial
import time
import sys
ser=serial.Serial('/dev/ttyUSB0',9600)
ser.close()
ser.open()
time.sleep(1)
sys.stdout.flush()
ser.flushInput()
ser.flushOutput()
while True:
 
    c=raw_input("enter A for tmperature of house1 and B for humidity, enter C for temperature of house2 and D for humidity:")
    ser.write((c))
    time.sleep(1)
    b=ser.read(ser.inWaiting())
    time.sleep(2)
    b=ser.read(ser.inWaiting())
    print 'receiving data is from:',c
    print 'receiving data is:',b
    sys.stdout.flush()
    ser.flushInput()
    ser.flushOutput()
    
    
    
