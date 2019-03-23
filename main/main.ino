#include "Wire.h"
#include <Stepper.h>
#include <Servo.h>
#include <SoftwareSerial.h>
#include <string.h>
#include "TFMini.h"

const int stepsPerRevolution = 400;  // change this to fit the number of steps per revolution
const int rowPoints = 20;
const int numberRows = 8;

// Setup software serial port 
SoftwareSerial mySerial(12, 13); // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
TFMini tfmini;
// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
// create servo object to control a servo
Servo myservo;

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(100);
  // attaches the servo on pin 6 to the servo object
  myservo.attach(6);
  // initialize the serial port:
  Serial.begin(9600);
  // Wait for serial port to connect. Needed for native USB port only
  while (!Serial);
  // Initialize the data rate for the SoftwareSerial port
  mySerial.begin(TFMINI_BAUDRATE);
  // Initialize the TF Mini sensor
  tfmini.begin(&mySerial);
}


void loop() {
  int data[numberRows*rowPoints];
  int index = 0;
  int sent = -1;
  
  // Take measurements 
  for (int i = 25; i < 115; i+= (90/(numberRows))){ // Servo control (25deg - 115deg)
    myservo.write(i);
    for (int j = 0; j < 400; j+= (400/rowPoints)){ // Stepper Motor control (0deg - 360deg)
      myStepper.step(400/rowPoints);       
      delay(100);
      // Record data point
      uint16_t dist = 100; //tfmini.getDistance(); 
      data[index] = dist;
      index += 1;
    }

    // Reset Stepper Motor to position 0    
    myStepper.step(-stepsPerRevolution);
    delay(500);
   }
  

  // Send data through serial COM
  for (int i = 0; i < sizeof(data)/sizeof(data[0]); i++){
    Serial.println(data[i]);    
  }
  Serial.println('EndOfData');
}
