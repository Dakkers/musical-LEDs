// This code is based off of the BoilerMake Badge template, which can be viewed at:
// https://github.com/BoilerMake/BoilerMakeBadge_I/blob/master/boilermakeBoard.cpp
// This requires the library for the RF24 radio thing, which can be found at:
// https://github.com/maniacbug/RF24

#include <RF24.h>
#include <SPI.h>
#include <EEPROM.h>

void setValue(word);
int SROEPin = 3; // using digital pin 3 for SR !OE
int SRLatchPin = 8; // using digital pin 4 for SR latch

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
  digitalWrite(SROEPin, LOW);
  setValue(0x3838);
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
