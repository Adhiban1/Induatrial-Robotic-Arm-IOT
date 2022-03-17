#include <Arduino.h>
#include <ESP32Servo.h>
#include <math.h>

Servo Servo0, Servo1, Servo2, Servo3, Servo4, Servo5;

int s0_pin = 13, s1_pin = 12, s2_pin = 14, s3_pin = 27, s4_pin = 26, s5_pin = 25;
double arm_length = 1;

class Arm
{
public:
    Arm(int s0 = 13, int s1 = 12, int s2 = 14, int s3 = 27, int s4 = 26, int s5 = 25, double l = 1)
    {
        s0_pin = s0;
        s1_pin = s1;
        s2_pin = s2;
        s3_pin = s3;
        s4_pin = s4;
        s5_pin = s5;
        arm_length = l;
    }

    void attach()
    {
        Servo0.attach(s0_pin);
        Servo1.attach(s1_pin);
        Servo2.attach(s2_pin);
        Servo3.attach(s3_pin);
        Servo4.attach(s4_pin);
        Servo5.attach(s5_pin);
    }

    void same_angles(double angle)
    {
        Servo0.write(angle);
        Servo1.write(angle);
        Servo2.write(angle);
        Servo3.write(angle);
        Servo4.write(angle);
        Servo5.write(angle);
    }
};

Arm arm;

void setup()
{
    Serial.begin(9600);
    arm.attach();
}

void loop()
{
    arm.same_angles(80);
    Serial.println("0");
    delay(1000);
    arm.same_angles(100);
    Serial.println("180");
    delay(1000);
}
