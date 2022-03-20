#include <Arduino.h>

void setup()
{
    Serial.begin(9600);
}

int ser = -1;
double x = 1, y = 1, z = 1, change = 0.01;
void function1()
{
    ser = Serial.read();
    Serial.print(x);
    Serial.print(", ");
    Serial.print(y);
    Serial.print(", ");
    Serial.println(z);
    if (ser == 100) // D
    {
        x += change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            x -= change;
        if (x > 2)
            x = 2;
    }
    else if (ser == 97) // A
    {
        x -= change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            x += change;
        if (x < -2)
            x = -2;
    }
    else if (ser == 119) // W
    {
        y += change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            y -= change;
        if (y > 2)
            y = 2;
    }
    else if (ser == 115) // S
    {
        y -= change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            y += change;
        if (y < 0)
            y = 0;
    }
    else if (ser == 114) // R
    {
        z += change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            z -= change;
        if (z > 2)
            z = 2;
    }
    else if (ser == 102) // F
    {
        z -= change;

        if ((sqrt(sq(x) + sq(y) + sq(z))) > 2)
            z += change;
        if (z < 0)
            z = 0;
    }
}

void loop()
{
}