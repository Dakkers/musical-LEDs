// This code is based off of the BoilerMake Badge template, which can be viewed at:
// https://github.com/BoilerMake/BoilerMakeBadge_I/blob/master/boilermakeBoard.cpp
// This requires the library for the RF24 radio thing, which can be found at:
// https://github.com/maniacbug/RF24

#include <RF24.h>
#include <SPI.h>
#include <EEPROM.h>
#include <stdio.h>
#include <stdlib.h>

void setValue(word);
int SROEPin = 3; // using digital pin 3 for SR !OE
int SRLatchPin = 8; // using digital pin 4 for SR latch

char del, ledStr1, ledStr2, incomingByte;
int counter;

void setup() {
  Serial.begin(9600);

  // SPI initializations
  SPI.begin();
  SPI.setClockDivider(16); // Set SPI clock to 16 MHz / 16 = 1 MHz

  // Shift register pin initializations
  pinMode(SROEPin, OUTPUT);
  pinMode(SRLatchPin, OUTPUT);
  digitalWrite(SROEPin, HIGH);
  digitalWrite(SRLatchPin, LOW);
}

void loop() {
  // initial code is just some blinking LEDs
  char del[] = "000";
  char ledStr1[] = "00000000";
  char ledStr2[] = "00000000";
  counter = 0;

  // split the data appropriately
  while (Serial.available() > 0) {
    incomingByte = Serial.read();

    if (counter < 8)
      ledStr1[counter] = incomingByte;
    else if (counter > 8 && counter < 17)
      ledStr2[counter-9] = incomingByte;
    else if (counter > 18)
      del[counter-19] = incomingByte;

    counter++;
    
  }

  long int ledHex1 = strtol(ledStr1, NULL, 2);
  long int ledHex2 = strtol(ledStr2, NULL, 2);
  ledHex1 = ledHex1 << 8;
  
  word hexValue = (word) ledHex1 + ledHex2;

  digitalWrite(SROEPin, LOW);
  setValue(hexValue);
  delay(1000);
  setValue(0x0000);
  delay(1000);
  digitalWrite(SROEPin, HIGH);
}

// Sends word sized value to both SRs & latches output pins
void setValue(word value) {
  byte Hvalue = value >> 8;
  byte Lvalue = value & 0x00FF;
  SPI.transfer(Lvalue);
  SPI.transfer(Hvalue);
  digitalWrite(SRLatchPin, HIGH);
  digitalWrite(SRLatchPin, LOW);
}
