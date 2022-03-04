#include <Arduino.h>
#include <ESP32Servo.h>
#include <math.h>

// Servos.
Servo myservo1;
#define PIN_SERVO1 13

// 'point_to_servoMove' changes the angles of servos when co-ordinate point is given.
double pi = 3.14159265359;

// dont give (0,0,0) point here then d2 becomes zero.
void point_to_servoMove(double x = 1, double y = 1, double z = 1, double l = 1) // x,y,z are the co-ordinates, l is the length of the arm.
{
    double d1, d2, a0, a1, a2, a4; // defining these all are as 'double'.
    if (x == 0 && y == 0)          // d1 should not be zero. 0 -> 0.001.
    {
        d1 = sqrt(pow(0.001, 2) + pow(0.001, 2));
    }
    else
    {
        d1 = sqrt(pow(x, 2) + pow(y, 2));
    }
    d2 = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    if (d2 < 2 * l) // if d2 > 2*l, then 'Out of Range'.
    {
        // these are the mathematical formulas.
        a0 = (acos(x / d1)) * 180 / pi;
        a1 = (acos(d1 / d2) + acos(d2 / (2 * l))) * 180 / pi;
        a2 = (pi - 2 * acos(d2 / (2 * l))) * 180 / pi;
        a4 = ((3 * pi / 2) - a1 - a2) * 180 / pi;
    }
    else
    {
        // this is set for default, when point goes to out of range.
        a0 = 90;
        a1 = 150;
        a2 = 60;
        a4 = 45;
    }

    // the angles are given to the servo motors.
    myservo1.write(a1);
    Serial.println(a1);
};

// Setup function.
void setup()
{ // Servos.
    myservo1.attach(PIN_SERVO1);

    // Serial Moniter.
    Serial.begin(9600);
}

int delay1 = 1000; // it is used to set the delay time between each moves.

// this the main loop function. Program inside it continuesly looping.
void loop()
{
    point_to_servoMove(); // default point of (1,1,1)
    delay(delay1);
    point_to_servoMove(1.46, 1.11, 0.52); // floating values are also applicable.
    delay(delay1);
    point_to_servoMove(1.46, 1.11, 0.52, 2); // here the 4th argument is length of the arm.
    delay(delay1);
}