#include <Arduino.h>
#include <ESP32Servo.h>

#define PIN_SERVO 13
Servo myservo;

void setup()
{
  myservo.attach(PIN_SERVO);
}

void loop()
{
  for (int pos = 90; pos <= 180; pos += 180)
  {
    myservo.write(pos);
    delay(500);
  }

  myservo.write(0);
  delay(1000);
}