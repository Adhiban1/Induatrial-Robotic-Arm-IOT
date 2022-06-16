#include <WiFi.h>
#include <Arduino.h>

const char *ssid = "ESP32 Access Point";
const char *password = "123456789";

WiFiServer server(80);

void setup()
{
    Serial.begin(9600);
    pinMode(2, OUTPUT);
    pinMode(13, OUTPUT);
    delay(1000);

    WiFi.softAP(ssid, password);
    IPAddress IP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(IP);
    server.begin();
}

void loop()
{

    WiFiClient client = server.available();

    if (client)
    {

        while (client.connected())
        {
            while (client.available() > 0)
            {

                int s = client.read();
                if (s == 110) // n
                {
                    digitalWrite(13, HIGH);
                    digitalWrite(2, HIGH);
                }
                else if (s == 102) // f
                {
                    digitalWrite(13, LOW);
                    digitalWrite(2, LOW);
                }
            }
            delay(10);
        }

        client.stop();
        Serial.println("Client disconnected");
    }
}