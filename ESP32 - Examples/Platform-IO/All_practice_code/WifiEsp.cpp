#include <Arduino.h>
#include "WiFi.h"

#define WIFI_NETWORK "Heisenberg's WiFi"
#define WIFI_PASSWORD "%q$jJeGIK#GgLlg#"
#define WIFI_TIMEOUT_MS 20000

void connectToWifi()
{
  Serial.print("Connecting to Wifi...");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_NETWORK, WIFI_PASSWORD);

  unsigned long startAttemtTime = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - startAttemtTime < WIFI_TIMEOUT_MS)
  {
    Serial.print(".");
    delay(100);
  }

  if (WiFi.status() != WL_CONNECTED)
  {
    Serial.println("  Failed");
  }
  else
  {
    Serial.println("  Connected.");
    Serial.println(WiFi.localIP());
  }
}

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  connectToWifi();
}

void loop()
{
  // put your main code here, to run repeatedly:
}