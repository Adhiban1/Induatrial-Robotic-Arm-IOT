#include <Arduino.h>
#include <ESP32Servo.h>

// using two touch we can control three actions.

Servo servo;

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
    servo.attach(13);
}

int threshold = 25;

void loop()
{
    int incr, decr;
    incr = touchRead(12);
    decr = touchRead(14);
    Serial.print("Touch (12): ");
    Serial.print(incr);
    Serial.print(", Touch (14): ");
    Serial.println(decr);
    if (incr < threshold && decr < threshold)
    {
        servo.write(90);
        digitalWrite(2, HIGH);
        delay(200);
        digitalWrite(2, LOW);
    }
    else if (incr < threshold)
    {
        servo.write(180);
        digitalWrite(2, HIGH);
        delay(200);
        digitalWrite(2, LOW);
    }
    else if (decr < threshold)
    {
        servo.write(0);
        digitalWrite(2, HIGH);
        delay(200);
        digitalWrite(2, LOW);
    }

    delay(500);
}
