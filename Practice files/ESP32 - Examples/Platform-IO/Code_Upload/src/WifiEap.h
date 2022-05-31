#include <Arduino.h>
#include <WiFi.h>

const char *ssid = "ESP32 Access Point";
const char *password = "123456789";

WiFiServer server(80);

void setup()
{
    Serial.begin(9600);
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
            if (client.available())
            {                           // if there's bytes to read from the client,
                char c = client.read(); // read a byte, then
                Serial.println(c);
            }
        }
    }
}