#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo;
int servo_pin = 13;
int random_angle;
int LED = 2;

void setup()
{
    Serial.begin(9600);
    pinMode(LED, OUTPUT);
    servo.attach(servo_pin);
}

double x, y, z, d;

void loop()
{
    random_angle = random(0, 10) * 10;
    Serial.println(random_angle);
    servo.write(random_angle);
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);

    // Random point.
    while (true)
    {
        x = random(0, 2000) / 1000.0;
        y = random(0, 2000) / 1000.0;
        z = random(0, 2000) / 1000.0;
        d = sqrt(sq(x) + sq(y) + sq(z));
        if (d < 2)
            break;
    }
    Serial.print("x: ");
    Serial.print(x);
    Serial.print(", y: ");
    Serial.print(y);
    Serial.print(", z: ");
    Serial.println(z);
    //----------------

    delay(1000);
}
