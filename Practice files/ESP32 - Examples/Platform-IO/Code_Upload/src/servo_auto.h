#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
    Serial.println("\nFirst click the curse on Serial Monitor,\nPress a,s,w,d,z,x.\na: Degree -\ns: degree +\nw: Record the Degree\nd: Automate\nz: Repeat -\nx: Repeat +\nDegree range: [0,180]\nRepeat range: [1,10]\n");
}

int degree = 0, i = -1, repeat = 3, max_repeat = 10;
int degree_list[10];

void loop()
{
    servo.write(degree);
    int msg = Serial.read();
    // Serial.println(degree);
    if (msg == 97) // a
    {
        degree--;
        if (degree < 0)
            degree = 0;
    }
    if (msg == 115) // s
    {
        degree++;
        if (degree > 180)
            degree = 180;
    }
    if (msg == 119) // w save
    {
        if (i < 9)
        {
            i++;
            degree_list[i] = degree;
            Serial.println("Degree Saved " + String(i + 1) + " = " + String(degree));
        }
    }
    if (msg == 122) // z decrease repeat
    {
        repeat--;
        if (repeat < 1)
            repeat = 1;
        Serial.println("Repeat: " + String(repeat));
    }
    if (msg == 120) // x increase repeat
    {
        repeat++;
        if (repeat > max_repeat)
            repeat = 10;
        Serial.println("Repeat: " + String(repeat));
    }
    if (msg == 100) // d automate
    {
        Serial.println("--------");
        for (int k = 0; k < repeat; k++)
        {
            for (int j = 0; j <= i; j++)
            {
                servo.write(degree_list[j]);
                Serial.println("Servo Angle " + String(j + 1) + ": " + String(degree_list[j]));
                delay(1000);
            }
            Serial.println("----------");
        }
        i = -1;
    }
}