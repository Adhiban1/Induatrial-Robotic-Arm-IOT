#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    servo.attach(13);
    Serial.begin(9600);
}

int a = 1000;

void loop()
{
    int s = Serial.read();
    Serial.println(a);
    if (s == 97) // a
    {
        a -= 100;
    }
    if (s == 115) // s
    {
        a += 100;
    }
    servo.write(0);
    delay(a);
    servo.write(180);
    delay(a);
}