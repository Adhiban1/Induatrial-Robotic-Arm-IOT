#include <Arduino.h>
#include <ESP32Servo.h>

#define PIN_SERVO 13
Servo myservo;

void setup()
{
  myservo.attach(PIN_SERVO1);
}

void loop()
{
  for (int pos = 0; pos <= 180; pos += 10)
  {
    myservo.write(pos);
    delay(500);
  }

  myservo.write(0);
  delay(1000);
}