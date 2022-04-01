#include <Arduino.h>
// #include <ESP32Servo.h>

// Servo servo;

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
}

void loop()
{
    if (Serial.available() > 0)
    {
        int msg = Serial.read();
        // Serial.println(msg);
        if (msg == 97)
            digitalWrite(2, HIGH);
        if (msg == 115)
            digitalWrite(2, LOW);
    }
}
