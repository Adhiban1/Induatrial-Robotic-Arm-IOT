#include <Keypad.h>
#include <Arduino.h>
#include <ESP32Servo.h>
#include <math.h>

float pi = 3.14159265359;

Servo base, sholder, elbow, wrist_r, wrist_ud, finger;

const byte ROWS = 4; // four rows
const byte COLS = 4; // three columns
char keys[ROWS][COLS] = {
    {'1', '2', '3', 'A'},
    {'4', '5', '6', 'B'},
    {'7', '8', '9', 'C'},
    {'*', '0', '#', 'D'}};
byte rowPins[ROWS] = {13, 12, 14, 27}; // connect to the row pinouts of the kpd
byte colPins[COLS] = {26, 25, 33, 32}; // connect to the column pinouts of the kpd

Keypad kpd = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup()
{
    Serial.begin(9600);
    base.attach(15);
    sholder.attach(4);
    elbow.attach(5);
    wrist_r.attach(18);
    wrist_ud.attach(19);
    finger.attach(21);
    pinMode(2, OUTPUT);
}

float x0 = 0, y2 = 0, z0 = 12, d1, a0, d2, m, l = 12, t1, t2, a1, a2, change = 1, rservo = 0, uservo = 45, fservo = 150;
float x_list[100], y_list[100], z_list[100], rservoList[100], uservoList[100], fservoList[100];
int c = -1, msg;

void positions()
{
    Serial.print("x:");
    Serial.print(x0);
    Serial.print(", ");
    Serial.print("y:");
    Serial.print(y2);
    Serial.print(", ");
    Serial.print("z:");
    Serial.print(z0);
    Serial.print(", ");
    Serial.print("r:");
    Serial.print(rservo);
    Serial.print(", ");
    Serial.print("u:");
    Serial.print(uservo);
    Serial.print(", ");
    Serial.print("f:");
    Serial.print(fservo);
    // Serial.print(", ");
    // Serial.print("a0:");
    // Serial.print(a0);
    // Serial.print(", ");
    // Serial.print("a1:");
    // Serial.print(a1);
    // Serial.print(", ");
    // Serial.print("a2:");
    // Serial.print(a2);
    if (sqrt(sq(x0) + sq(y2) + sq(z0)) >= 2 * l)
    {
        Serial.print(", [Invalid Point] [Don't press 'z']");
    }
    Serial.println("");
}

void formulas()
{
    d1 = sqrt(sq(x0) + sq(y2));
    a0 = acos(x0 / d1);
    d2 = sqrt(sq(x0) + sq(y2) + sq(z0));
    m = d2 / 2;
    t1 = acos(m / l);
    t2 = acos(d1 / d2);
    a1 = t1 + t2;
    a2 = pi - 2 * t1;
}

void degree()
{
    a0 *= (180 / pi);
    a1 *= (180 / pi);
    a2 *= (180 / pi);
}

void keypadControl()
{
    if (kpd.getKeys())
        for (int i = 0; i < LIST_MAX; i++)
            if (kpd.key[i].stateChanged)
            {
                int a = kpd.key[i].kcode;
                if (a == 0 && kpd.key[i].kstate == 1)
                {
                    x0 += change;
                    if (x0 > 2 * l)
                    {
                        x0 = 2 * l;
                    }
                }
                if (a == 4 && kpd.key[i].kstate == 1)
                {
                    x0 -= change;
                    if (x0 < -2 * l)
                    {
                        x0 = -2 * l;
                    }
                }
                if (a == 1 && kpd.key[i].kstate == 1)
                {
                    y2 += change;
                    if (y2 > 2 * l)
                    {
                        y2 = 2 * l;
                    }
                }
                if (a == 5 && kpd.key[i].kstate == 1)
                {
                    y2 -= change;
                    if (y2 < 0)
                    {
                        y2 = 0;
                    }
                }
                if (a == 2 && kpd.key[i].kstate == 1)
                {
                    z0 += change;
                    if (z0 > 2 * l)
                    {
                        z0 = 2 * l;
                    }
                }
                if (a == 6 && kpd.key[i].kstate == 1)
                {
                    z0 -= change;
                    if (z0 < 0)
                    {
                        z0 = 0;
                    }
                }
                if (a == 8 && kpd.key[i].kstate == 1)
                {
                    rservo++;
                    if (rservo > 180)
                        rservo = 180;
                }
                if (a == 12 && kpd.key[i].kstate == 1)
                {
                    rservo--;
                    if (rservo < 0)
                        rservo = 0;
                }
                if (a == 9 && kpd.key[i].kstate == 1)
                {
                    uservo++;
                    if (uservo > 180)
                        uservo = 180;
                }
                if (a == 13 && kpd.key[i].kstate == 1)
                {
                    uservo--;
                    if (uservo < 0)
                        uservo = 0;
                }
                if (a == 10 && kpd.key[i].kstate == 1)
                {
                    fservo++;
                    if (fservo > 150)
                        fservo = 150;
                }
                if (a == 14 && kpd.key[i].kstate == 1)
                {
                    fservo--;
                    if (fservo < 90)
                        fservo = 90;
                }
                if (a == 15 && kpd.key[i].kstate == 1) // d
                {
                    digitalWrite(2, HIGH);
                    c++;
                    x_list[c] = x0;
                    y_list[c] = y2;
                    z_list[c] = z0;
                    rservoList[c] = rservo;
                    uservoList[c] = uservo;
                    fservoList[c] = fservo;
                    Serial.print(c + 1);
                    Serial.println(" Recorded...");
                    delay(1000);
                    digitalWrite(2, LOW);
                }
                if (a == 7 && kpd.key[i].kstate == 1)
                {
                    digitalWrite(2, HIGH);
                    if (a2 <= 135 && a2 >= 0 && sqrt(sq(x0) + sq(y2) + sq(z0)) < 2 * l)
                    {
                        Serial.println("Move...");
                        base.write(a0);
                        delay(200);
                        sholder.write(a1);
                        delay(200);
                        elbow.write(180 - a2);
                        // delay(200);
                        // wrist_r.write(rservo);
                        // delay(200);
                        // wrist_ud.write(uservo);
                        // delay(200);
                        // finger.write(fservo);
                        delay(1000);
                    }
                    else
                    {
                        Serial.println("[Invalid]");
                        delay(1000);
                    }
                    digitalWrite(2, LOW);
                }
                if (a == 3 && kpd.key[i].kstate == 1)
                {
                    digitalWrite(2, HIGH);
                    Serial.println("Automation");
                    for (int k = 0; k < 3; k++)
                    {
                        for (int i = 0; i <= c; i++)
                        {
                            x0 = x_list[i];
                            y2 = y_list[i];
                            z0 = z_list[i];
                            formulas();
                            degree();
                            base.write(a0);
                            delay(200);
                            sholder.write(a1);
                            delay(200);
                            elbow.write(180 - a2);
                            // delay(200);
                            // wrist_r.write(rservoList[i]);
                            // delay(200);
                            // wrist_ud.write(uservoList[i]);
                            // delay(200);
                            // finger.write(fservoList[i]);
                            delay(2000);
                        }
                        Serial.print(k + 1);
                        Serial.println("time complete");
                    }
                    digitalWrite(2, LOW);
                }
                if (a == 11 && kpd.key[i].kstate == 1)
                {
                    digitalWrite(2, HIGH);
                    Serial.println("Cleared...");
                    c = -1;
                    delay(1000);
                    digitalWrite(2, LOW);
                }
            }
}

void serialControl()
{
    if (Serial.available())
    {
        msg = Serial.read();

        if (msg == 97) // a
        {
            x0 -= change;
            if (x0 < -2 * l)
            {
                x0 = -2 * l;
            }
        }
        if (msg == 100) // d
        {
            x0 += change;
            if (x0 > 2 * l)
            {
                x0 = 2 * l;
            }
        }
        if (msg == 119) // w
        {
            y2 += change;
            if (y2 > 2 * l)
            {
                y2 = 2 * l;
            }
        }
        if (msg == 115) // s
        {
            y2 -= change;
            if (y2 < 0)
            {
                y2 = 0;
            }
        }
        if (msg == 114) // r
        {
            z0 += change;
            if (z0 > 2 * l)
            {
                z0 = 2 * l;
            }
        }
        if (msg == 102) // f
        {
            z0 -= change;
            if (z0 < 0)
            {
                z0 = 0;
            }
        }
        if (msg == 113) // q
        {
            digitalWrite(2, HIGH);
            c++;
            x_list[c] = x0;
            y_list[c] = y2;
            z_list[c] = z0;
            rservoList[c] = rservo;
            uservoList[c] = uservo;
            fservoList[c] = fservo;
            Serial.print(c + 1);
            Serial.println(" Recorded...");
            delay(1000);
            digitalWrite(2, LOW);
        }
        if (msg == 122) // z
        {
            digitalWrite(2, HIGH);
            if (a2 <= 135 && a2 >= 0 && sqrt(sq(x0) + sq(y2) + sq(z0)) < 2 * l)
            {
                Serial.println("Move...");
                base.write(a0);
                delay(200);
                sholder.write(a1);
                delay(200);
                elbow.write(180 - a2);
                delay(200);
                wrist_r.write(rservo);
                delay(200);
                wrist_ud.write(uservo);
                delay(200);
                finger.write(fservo);
                delay(1000);
            }
            else
            {
                Serial.println("[Invalid]");
                delay(1000);
            }
            digitalWrite(2, LOW);
        }
        if (msg == 116) // t
        {
            rservo++;
            if (rservo > 180)
                rservo = 180;
        }
        if (msg == 103) // g
        {
            rservo--;
            if (rservo < 0)
                rservo = 0;
        }
        if (msg == 121) // y
        {
            uservo++;
            if (uservo > 180)
                uservo = 180;
        }
        if (msg == 104) // h
        {
            uservo--;
            if (uservo < 0)
                uservo = 0;
        }
        if (msg == 117) // u
        {
            fservo++;
            if (fservo > 150)
                fservo = 150;
        }
        if (msg == 106) // j
        {
            fservo--;
            if (fservo < 90)
                fservo = 90;
        }
        if (msg == 101) // e
        {
            digitalWrite(2, HIGH);
            Serial.println("Automation");
            for (int k = 0; k < 3; k++)
            {
                for (int i = 0; i <= c; i++)
                {
                    x0 = x_list[i];
                    y2 = y_list[i];
                    z0 = z_list[i];
                    formulas();
                    degree();
                    base.write(a0);
                    delay(200);
                    sholder.write(a1);
                    delay(200);
                    elbow.write(180 - a2);
                    delay(200);
                    wrist_r.write(rservoList[i]);
                    delay(200);
                    wrist_ud.write(uservoList[i]);
                    delay(200);
                    finger.write(fservoList[i]);
                    delay(2000);
                }
                Serial.print(k + 1);
                Serial.println("time complete");
            }
            digitalWrite(2, LOW);
        }
        if (msg == 99) // c
        {
            digitalWrite(2, HIGH);
            Serial.println("Cleared...");
            c = -1;
            delay(1000);
            digitalWrite(2, LOW);
        }
        if (msg == 120) // x
        {
            x0 = 0;
            y2 = 0;
            z0 = 12;
            fservo = 150;
            rservo = 0;
            uservo = 45;
        }
    }
}

void loop()
{
    positions();
    formulas();
    degree();
    keypadControl();
    serialControl();
}