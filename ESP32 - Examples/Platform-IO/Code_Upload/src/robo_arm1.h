#include <Arduino.h>
#include <ESP32Servo.h>
#include <math.h>

Servo Servo0, Servo1, Servo2, Servo3, Servo4, Servo5;

class Arm
{
public:
    double arm_length;
    int s1_pin, s2_pin, s3_pin, s4_pin, s5_pin, s6_pin;

    Arm(int s1, int s2, int s3, int s4, int s5, int s6, double l = 1)
    {
        s1_pin = s1;
        s2_pin = s2;
        s3_pin = s3;
        s4_pin = s4;
        s5_pin = s5;
        s6_pin = s6;
        Servo0.attach(s1_pin);
        Servo1.attach(s1_pin);
        Servo2.attach(s1_pin);
        Servo3.attach(s1_pin);
        Servo4.attach(s1_pin);
        Servo5.attach(s1_pin);
        Serial.begin(9600);
    }

    void write(double a0, double a1, double a2, double a3, double a4, double a5)
    {
        Servo0.write(a0);
        Servo1.write(a1);
        Servo2.write(a2);
        Servo3.write(a3);
        Servo4.write(a4);
        Servo5.write(a5);
        Serial.println("Angles:");
        Serial.println(a0);
        Serial.println(a1);
        Serial.println(a2);
        Serial.println(a3);
        Serial.println(a4);
        Serial.println(a5);
        Serial.println("---------------");
    }
};

void setup()
{
    Arm arm(1, 2, 3, 4, 5, 6);
    arm.write(45, 45, 45, 45, 45, 45);
}

void loop()
{
}