
this code receives the data from raspberry pi on rs485 and sends it back
#include <SoftwareSerial.h>
/*-----( Declare Constants and Pin Numbers )-----*/
#define SSerialRX        10  //Serial Receive pin
#define SSerialTX        11
#define SSerialTxControl 3 //RS485 SSerialTxControl control
#define RS485Transmit    HIGH
#define RS485Receive     LOW

#define Pin13LED         13

/*-----( Declare objects )-----*/



SoftwareSerial RS485Serial(SSerialRX, SSerialTX); // RX, TX

/*-----( Declare Variables )-----*/

char bytesend;

void setup()
{
  Serial.begin(9600);
  
  pinMode(Pin13LED, OUTPUT);   
  pinMode(SSerialTxControl, OUTPUT);  

  RS485Serial.begin(9600);
}

void loop()
{ 
  if(RS485Serial.available())
  {
  bytesend =RS485Serial.read();
 //Serial.print("I AM");
  //digitalWrite(Pin13LED,HIGH);
  delay(100);
  digitalWrite(SSerialTxControl,RS485Transmit);
  delay(600);
  RS485Serial.write(bytesend);
  Serial.print(bytesend);
  //digitalWrite(Pin13LED,LOW);
  digitalWrite(SSerialTxControl, RS485Receive); 
  }
}
