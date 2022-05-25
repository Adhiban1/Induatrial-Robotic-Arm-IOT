#include <WiFi.h>
#include <Arduino.h>
#include <ESP32Servo.h>

Servo base, sholder, elbow, wrist_r, wrist_ud, gripper;

const char *ssid = "LAPTOP-0HJP7HLH 6895";
const char *password = "siddarth";

WiFiServer wifiServer(80);

void setup()
{
    base.attach(13);
    sholder.attach(12);
    elbow.attach(14);
    wrist_r.attach(27);
    wrist_ud.attach(26);
    gripper.attach(25);
    Serial.begin(9600);
    pinMode(2, OUTPUT);

    Serial.begin(9600);

    delay(1000);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi..");
    }

    Serial.println("Connected to the WiFi network");
    Serial.println(WiFi.localIP());

    wifiServer.begin();
}

int baseAngle, sholderAngle, elbowAngle, wristRAngle, wristUAngle, gripperAngle;

void loop()
{

    WiFiClient client = wifiServer.available();

    if (client)
    {

        while (client.connected())
        {
            while (client.available() > 0)
            {

                String s = client.readString();
                baseAngle = s.substring(0, 3).toInt();
                sholderAngle = s.substring(3, 6).toInt();
                elbowAngle = s.substring(6, 9).toInt();
                wristRAngle = s.substring(9, 12).toInt();
                wristUAngle = s.substring(12, 15).toInt();
                gripperAngle = s.substring(15, 18).toInt();
                digitalWrite(2, HIGH);
                base.write(baseAngle);
                delay(100);
                sholder.write(sholderAngle);
                delay(100);
                elbow.write(elbowAngle);
                delay(100);
                wrist_r.write(wristRAngle);
                delay(100);
                wrist_ud.write(wristUAngle);
                delay(100);
                gripper.write(gripperAngle);
                delay(100);
                digitalWrite(2, LOW);
            }
            delay(10);
        }

        client.stop();
        Serial.println("Client disconnected");
    }
}