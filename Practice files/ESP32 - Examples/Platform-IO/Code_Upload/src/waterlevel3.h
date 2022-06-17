#include <WiFi.h>
#include <Arduino.h>

const char *ssid = "ESP32 Access Point";
const char *password = "123456789";
const int trigPin = 12;
const int echoPin = 14;
#define SOUND_SPEED 0.034
long duration;
float distanceCm;
float maxlevel = 10;
float minlevel = 25;

WiFiServer server(80);

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
    pinMode(13, OUTPUT);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    delay(1000);

    WiFi.softAP(ssid, password);
    IPAddress IP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(IP);
    server.begin();
}
int inp = 0;
void loop()
{
    unsigned long time = millis();
    WiFiClient client = server.available();

    if (client)
    {
        while (client.connected())
        {
            if (client.available() > 0)
            {
                inp = client.read();
                if (inp == 97) // a
                {
                    digitalWrite(13, HIGH);
                    digitalWrite(2, HIGH);
                }
                else if (inp == 98) // b
                {
                    digitalWrite(13, LOW);
                    digitalWrite(2, LOW);
                }
            }
            digitalWrite(trigPin, LOW);
            delayMicroseconds(2);
            // Sets the trigPin on HIGH state for 10 micro seconds
            digitalWrite(trigPin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trigPin, LOW);
            // Reads the echoPin, returns the sound wave travel time in microseconds
            duration = pulseIn(echoPin, HIGH);
            // Calculate the distance
            distanceCm = duration * SOUND_SPEED / 2;
            if (millis() - time > 1000)
            {
                client.print(String(distanceCm));
                Serial.println(distanceCm);
                if (distanceCm < maxlevel && distanceCm > 0)
                {
                    digitalWrite(13, LOW);
                    digitalWrite(2, LOW);
                }
                else if (distanceCm > minlevel)
                {
                    digitalWrite(13, HIGH);
                    digitalWrite(2, HIGH);
                }
                time = millis();
            }
        }
        client.stop();
        Serial.println("Client disconnected");
    }
}