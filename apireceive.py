#parsing the MAC address from the API frames received from XBee module
import serial
import sqlite3
import RPi.GPIO as GPIO
import time
ser=serial.Serial('/dev/ttyUSB0',baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=None)
ser.close()
ser.open()

def get_temp_val(): #function to get api frames
    temp=[]
    time.sleep(2)
    for i in range(0,17):
        temp.append(ser.read(1))
    return temp
temp=get_temp_val()
temp1=[hex(ord(i)) for i in temp]
print temp1
a=[temp1[i] for i in range(5,12)] #separate out address frames.
print a
d=temp1[15:-1]   #separate out data frames.
print 'you sent',d
add=[]
address= ( int(0x13a20040bcdb9a)) #combining the address frames.
address=("%x" % address)
a=[int(x,16) for x in a]
add.append((a[5]<<8)|a[6])
p=4
q=16
r=0
for i in range(0,5):
    add.append((a[p]<<q)|add[r])
    p=p-1
    q=q+8
    r=r+1
a=str("%x" % add[-1])
print a
if address==a:
    print 'correct address'
else:
    print 'different address'
    

