#include <Arduino.h>
// #include <ESP32Servo.h>

// Servo servo;
void setup()
{
    Serial.begin(9600);
}

double x = 0, y = 0;

void loop()
{
    Serial.print("x: ");
    Serial.print(x);
    Serial.print(", y: ");
    Serial.println(y);
    int a = Serial.read();
    if (a == 119) // w
        y += 0.25;
    if (y > 2)
        y = 2;
    else if (a == 115) // s
        y -= 0.25;
    if (y < 0)
        y = 0;
    else if (a == 100) // d
        x += 0.25;
    if (x > 2)
        x = 2;
    else if (a == 97) // a
        x -= 0.25;
    if (x < -2)
        x = -2;
    delay(100);
}