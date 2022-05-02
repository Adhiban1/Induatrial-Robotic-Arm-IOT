#include <Arduino.h>
#include <ESP32Servo.h>

Servo downservo, upservo;

void setup()
{
    downservo.attach(13);
    upservo.attach(12);
    Serial.begin(9600);
}
int a = 2000;
void loop()
{
    downservo.write(150);
    delay(50);
    upservo.write(180 - 60);
    delay(a);
    downservo.write(90);
    delay(50);
    upservo.write(180 - 180);
    delay(a);
}