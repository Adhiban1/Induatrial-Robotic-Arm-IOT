#include <Arduino.h>
#include <ESP32Servo.h>

Servo base, sholder, elbow, wrist_r, wrist_ud, gripper;
void setup()
{
    base.attach(15);
    sholder.attach(4);
    elbow.attach(5);
    wrist_r.attach(18);
    wrist_ud.attach(19);
    gripper.attach(21);
    Serial.begin(9600);
    pinMode(2, OUTPUT);
}

int baseAngle = 0, sholderAngle = 135, elbowAngle = 135, wrist_rAngle = 0, wrist_udAngle = 45, gripperAngle = 150;
int baselist[100], sholderlist[100], elbowlist[100], wrist_rlist[100], wrist_udlist[100], gripperlist[100];
int c = -1;

void display()
{
    Serial.print(baseAngle);
    Serial.print(", ");
    Serial.print(sholderAngle);
    Serial.print(", ");
    Serial.print(elbowAngle);
    Serial.print(", ");
    Serial.print(wrist_rAngle);
    Serial.print(", ");
    Serial.print(wrist_udAngle);
    Serial.print(", ");
    Serial.print(gripperAngle);
    Serial.print(", ");
    Serial.print(c + 1);
    Serial.println(" positions recorded.");
}

void controls()
{
    int b = Serial.read();
    if (b == 97) // a
    {
        baseAngle--;
        if (baseAngle < 0)
            baseAngle = 0;
        base.write(baseAngle);
    }
    if (b == 113) // q
    {
        baseAngle++;
        if (baseAngle > 180)
            baseAngle = 180;
        base.write(baseAngle);
    }
    if (b == 115) // s
    {
        sholderAngle--;
        if (sholderAngle < 0)
            sholderAngle = 0;
        sholder.write(sholderAngle);
    }
    if (b == 119) // w
    {
        sholderAngle++;
        if (sholderAngle > 180)
            sholderAngle = 180;
        sholder.write(sholderAngle);
    }
    if (b == 100) // d
    {
        elbowAngle--;
        if (elbowAngle < 0)
            elbowAngle = 0;
        elbow.write(elbowAngle);
    }
    if (b == 101) // e
    {
        elbowAngle++;
        if (elbowAngle > 140)
            elbowAngle = 140;
        elbow.write(elbowAngle);
    }
    if (b == 102) // f
    {
        wrist_rAngle--;
        if (wrist_rAngle < 0)
            wrist_rAngle = 0;
        wrist_r.write(wrist_rAngle);
    }
    if (b == 114) // r
    {
        wrist_rAngle++;
        if (wrist_rAngle > 180)
            wrist_rAngle = 180;
        wrist_r.write(wrist_rAngle);
    }
    if (b == 103) // g
    {
        wrist_udAngle--;
        if (wrist_udAngle < 0)
            wrist_udAngle = 0;
        wrist_ud.write(wrist_udAngle);
    }
    if (b == 116) // t
    {
        wrist_udAngle++;
        if (wrist_udAngle > 180)
            wrist_udAngle = 180;
        wrist_ud.write(wrist_udAngle);
    }
    if (b == 104) // h
    {
        gripperAngle--;
        if (gripperAngle < 90)
            gripperAngle = 90;
        gripper.write(gripperAngle);
    }
    if (b == 121) // y
    {
        gripperAngle++;
        if (gripperAngle > 150)
            gripperAngle = 150;
        gripper.write(gripperAngle);
    }

    // if (b == 122) // z
    // {
    //     downservo.write(downservo_angle);
    //     delay(200);
    //     upservo.write(upservo_angle);
    //     delay(200);
    //     baseservo.write(baseservo_angle);
    //     Serial.println("Arm Moved");
    //     delay(200);
    // }
    if (b == 118) // v
    {
        digitalWrite(2, HIGH);
        c++;
        baselist[c] = baseAngle;
        sholderlist[c] = sholderAngle;
        elbowlist[c] = elbowAngle;
        wrist_rlist[c] = wrist_rAngle;
        wrist_udlist[c] = wrist_udAngle;
        gripperlist[c] = gripperAngle;
        // Serial.print("Recorded ");
        Serial.println(c + 1);
        delay(1000);
        digitalWrite(2, LOW);
    }
    if (b == 122) // z
    {
        digitalWrite(2, HIGH);
        Serial.println("Default Position...");
        baseAngle = 0, sholderAngle = 135, elbowAngle = 135, wrist_rAngle = 0, wrist_udAngle = 45, gripperAngle = 150;
        base.write(baseAngle);
        delay(100);
        sholder.write(sholderAngle);
        delay(100);
        elbow.write(elbowAngle);
        delay(100);
        wrist_r.write(wrist_rAngle);
        delay(100);
        wrist_ud.write(wrist_udAngle);
        delay(100);
        gripper.write(gripperAngle);
        delay(1000);
        digitalWrite(2, LOW);
    }
    if (b == 120) // x
    {
        digitalWrite(2, HIGH);
        if (c >= 0)
        {
            for (int k = 0; k < 3; k++)
            {
                Serial.print(k + 1);
                Serial.println("------");
                for (int i = 0; i <= c; i++)
                {
                    base.write(baseAngle);
                    delay(100);
                    sholder.write(sholderAngle);
                    delay(100);
                    elbow.write(elbowAngle);
                    delay(100);
                    wrist_r.write(wrist_rAngle);
                    delay(100);
                    wrist_ud.write(wrist_udAngle);
                    delay(100);
                    gripper.write(gripperAngle);
                    delay(2000);
                }
            }
        }
        else
        {
            Serial.println("No recored positions, or only one position...");
        }
        digitalWrite(2, LOW);
    }
    if (b == 99) // c
    {
        digitalWrite(2, HIGH);
        c = -1;
        Serial.println("Cleared...");
        delay(1000);
        digitalWrite(2, LOW);
    }
}

void loop()
{

    if (Serial.available())
    {
        display();
        controls();
    }
}