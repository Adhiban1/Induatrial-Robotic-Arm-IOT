#include <Arduino.h>

void setup()
{
    Serial.begin(9600);
}

float x = 0, y = 0, z = 0;
int i = 0;
float x_list[100], y_list[100], z_list[100];
void loop()
{
    Serial.println("(" + String(x) + ", " + String(y) + ", " + String(z) + ")");
    int msg = Serial.read();
    if (msg == 119) // w
        y += 0.1;
    if (msg == 115) // s
        y -= 0.1;
    if (msg == 97) // a
        x -= 0.1;
    if (msg == 100) // d
        x += 0.1;
    if (msg == 114) // r
        z += 0.1;
    if (msg == 102) // f
        z -= 0.1;
    if (msg == 113) // q
    {
        x_list[i] = x;
        y_list[i] = y;
        z_list[i] = z;
        i++;
        if (i > 99)
            i = 99;
    }
    if (msg == 122) // z
    {
        for (int j = 0; j <= i; j++)
        {
            Serial.println(String(x_list[j]) + ", " + String(y_list[j]) + ", " + String(z_list[j]));
        }
        i = 0;
        delay(5000);
    }
}