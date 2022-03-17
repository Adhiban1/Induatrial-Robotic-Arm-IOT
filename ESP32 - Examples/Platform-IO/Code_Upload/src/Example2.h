#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
    servo.attach(13);
}

void loop()
{
    Serial.print("Touch: ");
    Serial.println(touchRead(12));
    if (touchRead(12) < 60)
    {
        servo.write(180);
        digitalWrite(2, HIGH);
        Serial.println("--------180--------");
        // delay(1000);
    }
    else
    {
        servo.write(0);
        digitalWrite(2, LOW);
    }
    delay(50);
}
