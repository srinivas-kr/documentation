#include<stdib.h>
#define RS485Transmit  HIGH
#define RS485Receive   LOW
#define Direction  4
#define Pin13LED    13
char bytesend;
void setup()
{
  Serial.begin(9600);
  
  pinMode(Pin13LED, OUTPUT);   
  pinMode(Direction, OUTPUT);
  pinMode(Pin13LED, LOW);
  digitalWrite(Direction,RS485Receive);
}
 
void loop()
{ 
  if(Serial.available())
  {
 // digitalWrite(Pin13LED,LOW);
  bytesend =Serial.read();
  delay(100);
  //digitalWrite(Pin13LED,HIGH);
  digitalWrite(Direction,RS485Transmit);
  delay(1000);
  Serial.write(bytesend);
 // digitalWrite(Pin13LED,LOW);
  digitalWrite(Direction,RS485Receive);
  
}
}
