#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    servo.attach(13);
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available())
    {
        String s = Serial.readString();
        servo.write(s.toInt());
    }
}