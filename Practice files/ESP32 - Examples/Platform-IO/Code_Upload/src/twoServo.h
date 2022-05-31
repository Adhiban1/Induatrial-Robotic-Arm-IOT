#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo1, servo2, servo3;

void setup()
{
    servo1.attach(13);
    servo2.attach(12);
    servo3.attach(14);
}

void loop()
{
    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(1000);
    servo1.write(80);
    servo2.write(80);
    servo3.write(80);
    delay(1000);
}