#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;
void setup()
{
    servo.attach(13);
    Serial.begin(9600);
}

int msg, angle = 0;

void loop()
{
    Serial.println(angle);
    if (Serial.available())
    {
        msg = Serial.read();
        if (msg == 115) // s
        {
            angle++;
            // servo.attach(13);
            servo.write(angle);
            // servo.detach();
        }
        if (msg == 97) // a
        {
            angle--;
            // servo.attach(13);
            servo.write(angle);
            // servo.detach();
        }
    }
}