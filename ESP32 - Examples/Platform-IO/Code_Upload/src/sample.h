#include <Arduino.h>
// #include <ESP32Servo.h>

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available())
    {
        Serial.println(Serial.read());
    }
}