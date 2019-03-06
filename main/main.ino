#include "Wire.h"
#include <Stepper.h>
#include <Servo.h>
#include <SoftwareSerial.h>
#include "TFMini.h"

const int stepsPerRevolution = 400;  // change this to fit the number of steps per revolution

// Setup software serial port 
SoftwareSerial mySerial(0, 1); // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
TFMini tfmini;
// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
// create servo object to control a servo
Servo myservo;

int data[30];
int counter = 0;
const int rowPoints = 5;
const int numberRows = 5;

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(100);
  // attaches the servo on pin 6 to the servo object
  myservo.attach(6);
  // initialize the serial port:
  Serial.begin(9600);
  // wait for serial port to connect. Needed for native USB port only
  while (!Serial);
  Serial.println ("Initializing...");
  //Initialize the data rate for the SoftwareSerial port
  mySerial.begin(TFMINI_BAUDRATE);
  //Initialize the TF Mini sensor
  tfmini.begin(&mySerial);
}

void loop() {
  // step one revolution  in one direction:
  Serial.println("clockwise");
  // set servo2 to 20 degrees start (range of motion 7 - 173)
  for (int i = 20; i <= 110; i += (90/numberRows)){
    myservo.write(i);
    //set servo1 to 
    for (int j = 0; j < 400; j+= (400/numberRows)){
      
      myStepper.step(20);
      delay(100);
      uint16_t dist = tfmini.getDistance(); 
      data[counter] = dist;
      counter += 1;
    }
    delay(500);
    // step one revolution in the other direction:
    Serial.println("counterclockwise");
    myStepper.step(-stepsPerRevolution);
    delay(500);
    }
}
