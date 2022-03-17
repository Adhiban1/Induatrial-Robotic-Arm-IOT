#include <Arduino.h>
#include <ESP32Servo.h>
#include <cmath>

Servo Servo0, Servo1, Servo2, Servo3, Servo4, Servo5;

int s0_pin = 13, s1_pin = 12, s2_pin = 14, s3_pin = 27, s4_pin = 26, s5_pin = 25;
double arm_length = 1;
double pi = 3.14159265359;

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

        Servo0.write(90);
        Servo1.write(150);
        Servo2.write(60);
        Servo3.write(0);
        Servo4.write(60);
        Servo5.write(45);
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

    double d1, a0, d2, m, t1, t2, a1, a2, a4; // Formula

    void point(double x1 = 1.0, double y1 = 1.0, double z1 = 1.0)
    {
        d2 = sqrt(pow(x1, 2) + pow(y1, 2) + pow(z1, 2));
        if (d2 < arm_length * 2 && d2 > 0)
        {
            // Formula ...................
            d1 = sqrt(pow(x1, 2) + pow(y1, 2));
            if (d1 == 0)
            {
                d1 = 0.0001;
            }
            a0 = acos(x1 / d1);

            m = d2 / 2;
            t1 = acos(m / arm_length);
            if (d2 == 0)
            {
                d2 = 0.0001;
            }
            t2 = acos(d1 / d2);
            a1 = t1 + t2;
            a2 = pi - 2 * t1;
            a4 = ((3 * pi / 2) - a1 - a2);
            // --------------------------

            // Converting Radian to degree.
            a0 = a0 * (180 / pi);
            a1 = a1 * (180 / pi);
            a2 = a2 * (180 / pi);
            a4 = a4 * (180 / pi);
            // ------------------------

            // Angles are given to Servos.
            Servo0.write(a0);
            Servo1.write(a1);
            Servo2.write(a2);
            Servo4.write(a4);
            // ------------------------
            Serial.println("point angles:");
            Serial.println(a0);
            Serial.println(a1);
            Serial.println(a2);
            Serial.println(a4);
            Serial.println("------------------------");
        }
        else
        {
            Serial.println("*****Invalid point*****");
        }
    }
};

Arm arm;

void setup()
{
    Serial.begin(9600);
    arm.attach();
    arm.point(1, 1, 1);
}

void loop()
{
}
