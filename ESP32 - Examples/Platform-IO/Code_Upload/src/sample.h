#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    servo.attach(13);
    // Serial.begin(9600);
}

int a = 3000;

void loop()
{
    servo.write(0);
    delay(a);
    servo.write(180);
    delay(a);
}