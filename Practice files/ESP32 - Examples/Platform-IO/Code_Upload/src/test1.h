#include <Arduino.h>
#include <ESP32Servo.h>

Servo downservo, upservo;

void setup()
{
    downservo.attach(13);
    upservo.attach(12);
    Serial.begin(9600);
}
// const int a = 2000;
int downservo_angle = 153, upservo_angle = 141;
int downservoAngles[10], upservoAngles[10];
int c = -1;
void loop()
{

    if (Serial.available())
    {
        Serial.print(downservo_angle);
        Serial.print(", ");
        Serial.print(upservo_angle);
        Serial.print(", ");
        Serial.print(c + 1);
        Serial.println(" positions recorded.");
        int b = Serial.read();
        if (b == 97) // a
            downservo_angle--;
        if (b == 115) // s
            downservo_angle++;
        if (b == 100) // d
            upservo_angle--;
        if (b == 102) // f
            upservo_angle++;
        if (b == 122) // z
        {
            downservo.write(downservo_angle);
            delay(100);
            upservo.write(upservo_angle);
            Serial.println("Arm Moved");
            delay(2000);
        }
        if (b == 114) // r
        {
            c++;
            downservoAngles[c] = downservo_angle;
            upservoAngles[c] = upservo_angle;
            Serial.print("Recorded ");
            Serial.println(c + 1);
            delay(2000);
        }
        if (b == 120) // x
        {
            if (c >= 0)
            {
                for (int k = 0; k < 3; k++)
                {
                    Serial.print(k + 1);
                    Serial.println("------");
                    for (int i = 0; i <= c; i++)
                    {
                        downservo.write(downservoAngles[i]);
                        delay(100);
                        upservo.write(upservoAngles[i]);
                        delay(2000);
                    }
                }
            }
            else
            {
                Serial.println("No recored positions");
            }
        }
        if (b == 113) // q
        {
            c = -1;
            Serial.println("Cleared...");
        }
    }
}