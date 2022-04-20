#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
}

void loop()
{
    String msg = Serial.readString();
    // Serial.println(msg);
    if (msg == "right")
    {
        servo.write(0);
    }
    if (msg == "left")
    {
        servo.write(180);
    }
}