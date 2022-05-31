#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
}

String str1 = "";

void loop()
{
    if (Serial.available())
    {
        int msg = Serial.read() - 48;
        Serial.print(msg);
        str1 += String(msg);

        if (str1.length() == 3)
        {
            Serial.print("\n");
            servo.write(str1.toInt());
            str1 = "";
            delay(1000);
        }
        delay(50);
    }
}