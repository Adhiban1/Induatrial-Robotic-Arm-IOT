#include <Arduino.h>

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
}

void loop()
{
    int touch = touchRead(13);
    Serial.println(touch);
    if (25 > touch)
    {
        digitalWrite(2, HIGH);
    }
    else
    {
        digitalWrite(2, LOW);
    }
    delay(100);
}