#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
    pinMode(2, OUTPUT);
    digitalWrite(2, LOW);
}

void loop()
{
    if (Serial.available() > 0)
    {
        String msg = Serial.readString();
        // Serial.println(msg);
        if (msg == "ON")
            digitalWrite(2, HIGH);
        else if (msg == "OFF")
            digitalWrite(2, LOW);
        else
        {
            servo.write(msg.toInt());
        }
    }
}
