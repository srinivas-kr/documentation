
# temperature and humidity data logging with repeater and updating the same data in sqlite3 database
#Author:Ruthvik Vaila
import serial
import time
import sys
import sqlite3
conn1=sqlite3.connect('temp1data.db')
conn2=sqlite3.connect('humid1data.db')
ser=serial.Serial('/dev/ttyUSB0',9600)
ser.close()
ser.open()
time.sleep(1)
sys.stdout.flush()
ser.flushInput()
ser.flushOutput()
a=['A','B']
while True:
    for i in range(0,2):
        c=a[i]
    #c=raw_input("enter A for tmperature of house1 and B for humidity, enter C for temperature of house2 and E for humidity:")
        ser.write((c))
        #time.sleep(0)
        #b=ser.read(1)
        #print b
        time.sleep(2.3)
        #b=ser.read(1) #(uncomment if using repeater)
        b=ser.read(ser.inWaiting())
        print 'receiving data is from:',c
        print 'receiving data is:',b
        sys.stdout.flush()
        sys.stdin.flush()
        #ser.flushInput()
        #ser.flushOutput()
        if i==0:
            c1=conn1.cursor()
            c1.execute("""INSERT INTO data values(date('now'),time('now'),(?))""",( b,))
            conn1.commit()
            
        else :
            c2=conn2.cursor()
            c2.execute("""INSERT INTO data values(date('now'),time('now'),(?))""",( b,))
            conn2.commit()
        
    
    
    
