import serial
import time
def send_temp_serially():    
    print "configuring and opening serial port" 
    ser=serial.Serial(15,9600,timeout=1)
    ser.close() #close if it is opened before
    ser.open()
    while True:
         # open the port
        temp=raw_input("enter temprature:")
        ser.write(temp)#send the value to pi
        print "wait lil bit"
        time.sleep(1)
send_temp_serially()
    
    
        
        
        
           
        
    
      
