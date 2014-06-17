
#include <DHT22.h>
// Only used for sprintf
#include <LiquidCrystal.h>
#include <stdio.h>
#include <string.h>
//for software uart

/*-----( Declare Constants and Pin Numbers )-----*/


//#define Direction 3   //RS485 Direction control
#define Transmit    HIGH
#define Receive     LOW

#define Pin13LED         13

// Data wire is plugged into port 7 on the Arduino
// Connect a 4.7K resistor between VCC and the data pin (strong pullup)
#define DHT22_PIN 7



// Setup a DHT22 instance
DHT22 myDHT22(DHT22_PIN);
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 6, 2);

/*-----( Declare objects )-----*/


/*-----( Declare Variables )-----*/
int byteReceived;
int byteSend;


void setup()   /****** SETUP: RUNS ONCE ******/
{
  // Start the built-in serial port, probably to Serial Monitor
  Serial.begin(9600);

  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  
  //pinMode(Pin13LED, OUTPUT);   
  pinMode(Pin13LED, OUTPUT);
  //pinMode(Direction,OUTPUT);
  digitalWrite(Pin13LED, HIGH);   
  
  lcd.setCursor(0,0);
  //lcd.print("Requesting data...");
  
  // Start the software serial port, to another device
 // RS485Serial.begin(4800);   // set the data rate 
}//--(end setup )---


void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
 
  //Serial.println("waiting for data.. ");
  //delay(2000);
  //Copy input data to output  
    
    
     //loop for get data from DHT22
   DHT22_ERROR_t errorCode;
  

  // set the cursor to column 0, line 1
 
  errorCode = myDHT22.readData();
  switch(errorCode)
  {
    case DHT_ERROR_NONE:
      lcd.clear();
      lcd.setCursor(0,1);
      lcd.print(myDHT22.getTemperatureC());

      Serial.write((byte)myDHT22.getTemperatureC());
      //lcd.setCursor(9,1);
      //lcd.print(myDHT22.getHumidity());
      //Serial.print(myDHT22.getHumidity());
      //lcd.print("%");
     // Serial.println("%");
      // Alternately, with integer formatting which is clumsier but more compact to store and
	  // can be compared reliably for equality:
	  //	  
      char buf[128];
      sprintf(buf, " %hi.%01hi ",
                   myDHT22.getTemperatureCInt()/10, abs(myDHT22.getTemperatureCInt()%10));
                   
      Serial.println(buf);
      break;
    case DHT_ERROR_CHECKSUM:
      Serial.print("check sum error ");
      Serial.print(myDHT22.getTemperatureC());
      //Serial.print(myDHT22.getHumidity());
      //Serial.println("%");
      break;
    //case DHT_BUS_HUNG:
      //Serial.println("BUS Hung ");
    //  break;
    //case DHT_ERROR_NOT_PRESENT:
      //Serial.println("Not Present ");
      //break;
    //case DHT_ERROR_ACK_TOO_LONG:
      //Serial.println("ACK time out ");
      //break;
  //  case DHT_ERROR_SYNC_TIMEOUT:
    //  Serial.println("Sync Timeout ");
      //break;
  //  case DHT_ERROR_DATA_TIMEOUT:
    //  Serial.println("Data Timeout ");
     // break;
    //case DHT_ERROR_TOOQUICK:
      //Serial.println("Polled to quick ");
      //break;/
  }
  
    
    //digitalWrite(SSerialTxControl, RS485Receive);  // Disable RS485 Transmit      
    // delay(100);
  } // End If RS485SerialAvailable
//(end main loop )---
