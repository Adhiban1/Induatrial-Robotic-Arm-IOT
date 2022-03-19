#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;
double degree = 0;
int increment = 90;

// 'W' & 'A' are used to increase and decrease the 'increment' value.
// 'S' & 'D' are used to decrease and increase the 'degree' value.
// type 'W', 'A', 'S' & 'D' only in Serial Monitor Terminal.
void servo_key_s_d()
{
    int ser = Serial.read();
    if (ser == 100) // d
    {
        degree += increment;
        if (degree > 180)
            degree = 180;
    }

    else if (ser == 115) // s
    {
        degree -= increment;
        if (degree < 0)
            degree = 0;
    }
    else if (ser == 119) // w
    {
        increment++;
        if (increment > 180)
            increment = 180;
    }
    else if (ser == 97)
    {
        increment--;
        if (increment < 1)
            increment = 1;
    }
    servo.write(degree);
    Serial.print("Degree: ");
    Serial.print(degree);
    Serial.print(", Change: ");
    Serial.println(increment);
    // delay(100);
}

// type '0' , '90', '50.25', and so on... in Serial Monitor Terminal to change the 'degree' value.
void servo_angle_input()
{
    double ser = Serial.readString().toDouble();
    if (ser > 0)
        degree = ser;
    servo.write(degree);
    Serial.println(degree);
    // delay(1000);
}

void setup()
{
    Serial.begin(9600);
    servo.attach(13);
}

void loop()
{
    // servo_angle_input();
    servo_key_s_d();
}