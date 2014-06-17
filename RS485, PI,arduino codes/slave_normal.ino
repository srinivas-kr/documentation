
/this code receives data from raspberry pi through UART(without rs485) and sends back
#define Pin13LED 13
#define Direction 2
#define Transmit HIGH
#define Receive LOW
int bytesend;
void setup(){
  Serial.begin(9600);
  pinMode(Pin13LED, OUTPUT);
  pinMode(Direction,OUTPUT); 
  digitalWrite(Pin13LED,LOW);
  digitalWrite(Direction,LOW);
}
void loop()
{
  if(Serial.available())
  {
  
    bytesend = Serial.read();
   
    digitalWrite(Pin13LED,HIGH);
    digitalWrite(Direction,HIGH);
   
    Serial.write(bytesend);
    digitalWrite(Pin13LED,LOW);
    digitalWrite(Direction,LOW);
  }
}
