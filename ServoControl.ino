#include "Wire.h"
/*
 Stepper Motor Control - one revolution

 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.

 The motor should revolve one revolution in one direction, then
 one revolution in the other direction.
 */

#include <Stepper.h>
#include <Servo.h>

const int stepsPerRevolution = 400;  // change this to fit the number of steps per revolution


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
// create servo object to control a servo
Servo myservo;
// variable to store the servo position
int pos = 0;

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(100);
  // attaches the servo on pin 6 to the servo object
  myservo.attach(6);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  // step one revolution  in one direction:
  Serial.println("clockwise");
  int x = 0;
  delay(100);
  // set servo2 to 7 degrees start because its broken
  for (pos = 7; pos <= 97; pos += 18){
    myservo.write(pos);
    for (int i = 1; i <= 20; i++){
      x = x + 1;
      Serial.println(x);
      myStepper.step(20);
      delay(500);
      /*MEASUREMENT*/  
    }
    delay(500);
    // step one revolution in the other direction:
    Serial.println("counterclockwise");
    myStepper.step(-stepsPerRevolution);
    delay(500);
    }
}
