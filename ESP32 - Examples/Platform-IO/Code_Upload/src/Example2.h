#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
}

int i = 0;

void loop()
{
    if (touchRead(12) < 20)
    {
        servo.write(i);
        Serial.println(i);
        i++;
        if (i == 181)
        {
            i = 0;
        }
    }
}