#include <Arduino.h>
#include <ESP32Servo.h>
#include <cmath>

// Creating Servo Objects.
Servo Servo0, Servo1, Servo2, Servo3, Servo4, Servo5;

// Set Servo pins.
int s0_pin = 13, s1_pin = 12, s2_pin = 14, s3_pin = 27, s4_pin = 26, s5_pin = 25;
double arm_length = 1; // Length of Arm.

double pi = 3.14159265359;
int LED = 2;

// Arm Class.
class Arm
{
public:
    // Constructor for Arm Class.
    Arm(int s0 = 13, int s1 = 12, int s2 = 14, int s3 = 27, int s4 = 26, int s5 = 25, double l = 1)
    {
        s0_pin = s0;
        s1_pin = s1;
        s2_pin = s2;
        s3_pin = s3;
        s4_pin = s4;
        s5_pin = s5;
        arm_length = l;
    }

    // use it in 'setup()' to initiate the connection and Arm default position.
    void attach()
    {
        Servo0.attach(s0_pin);
        Servo1.attach(s1_pin);
        Servo2.attach(s2_pin);
        Servo3.attach(s3_pin);
        Servo4.attach(s4_pin);
        Servo5.attach(s5_pin);
        pinMode(LED, OUTPUT);

        // Arm default position.
        Servo0.write(90);
        Servo1.write(150);
        Servo2.write(60);
        Servo3.write(0);
        Servo4.write(60);
        Servo5.write(45);
    }

    // Use this to move all servo at same angles.
    void same_angles(double angle)
    {
        Servo0.write(angle);
        Servo1.write(angle);
        Servo2.write(angle);
        Servo3.write(angle);
        Servo4.write(angle);
        Servo5.write(angle);
    }

    double d1, a0, d2, m, t1, t2, a1, a2, a4; // Formula

    // point to Servo move.
    void point(double x1 = 1.0, double y1 = 1.0, double z1 = 1.0)
    {
        d2 = sqrt(pow(x1, 2) + pow(y1, 2) + pow(z1, 2));
        if (d2 < arm_length * 2 && d2 > 0)
        {
            // Formula ...................
            d1 = sqrt(pow(x1, 2) + pow(y1, 2));
            if (d1 == 0)
            {
                d1 = 0.0001;
            }
            a0 = acos(x1 / d1);

            m = d2 / 2;
            t1 = acos(m / arm_length);
            if (d2 == 0)
            {
                d2 = 0.0001;
            }
            t2 = acos(d1 / d2);
            a1 = t1 + t2;
            a2 = pi - 2 * t1;
            a4 = ((3 * pi / 2) - a1 - a2);
            // --------------------------

            // Converting Radian to degree.
            a0 = a0 * (180 / pi);
            a1 = a1 * (180 / pi);
            a2 = a2 * (180 / pi);
            a4 = a4 * (180 / pi);
            // ------------------------

            // Angles are given to Servos.
            Servo0.write(a0);
            Servo1.write(a1);
            Servo2.write(a2);
            Servo4.write(a4);
            // ------------------------
            Serial.println("point angles:");
            Serial.println(a0);
            Serial.println(a1);
            Serial.println(a2);
            Serial.println(a4);
            Serial.println("------------------------");
        }
        else
        {
            Serial.println("*****Invalid point*****");
        }
        digitalWrite(LED, HIGH);
        delay(200);
        digitalWrite(LED, LOW);
    }

    // it will rotate wrist.
    void rotate(int a)
    {
        Servo3.write(a);
        Serial.print("Servo3 Angle: ");
        Serial.println(a);
    }

    // it will close the fingers of arm.
    void lock()
    {
        Servo5.write(0);
        Serial.println("Object locked");
    }

    // it will spread the fingers of arm.
    void unlock()
    {
        Servo5.write(90);
        Serial.println("Object unlocked");
    }

    double x, y, z, d;

    void rand_point() // Creates random valid point and that point given to the servos.
    {
        while (true)
        {
            x = random(-2000, 2000) / 1000.0;
            y = random(0, 2000) / 1000.0;
            z = random(0, 2000) / 1000.0;
            d = sqrt(sq(x) + sq(y) + sq(z));
            if (d < 2 && x != 0 && y > 0 && z > 0)
                break;
        }

        Serial.println("Random point:");
        Serial.print("x: ");
        Serial.print(x);
        Serial.print(", y: ");
        Serial.print(y);
        Serial.print(", z: ");
        Serial.println(z);
        Serial.println(" ");

        point(x, y, z);
    }

    double n;
    int div = 10;
    double x_arr[11], y_arr[11], z_arr[11];
    void move(double x1, double y1, double z1, double x2, double y2, double z2)
    {
        if (x1 != x2)
        {
            Serial.print("Moving from (");
            Serial.print(x1);
            Serial.print(", ");
            Serial.print(y1);
            Serial.print(", ");
            Serial.print(z1);
            Serial.print(") to (");
            Serial.print(x2);
            Serial.print(", ");
            Serial.print(y2);
            Serial.print(", ");
            Serial.print(z2);
            Serial.println(")");

            n = (x2 - x1) / div;
            x_arr[0] = x1;
            for (int i = 1; i < div + 1; i++)
                x_arr[i] = x_arr[i - 1] + n;
            for (int i = 0; i < div + 1; i++)
                y_arr[i] = (y2 - y1) * (x_arr[i] - x1) / (x2 - x1) + y1;
            for (int i = 0; i < div + 1; i++)
                z_arr[i] = (z2 - z1) * (x_arr[i] - x1) / (x2 - x1) + z1;

            for (int i = 0; i < div + 1; i++)
                point(x_arr[i], y_arr[i], z_arr[i]);
        }
        else if (y1 != y2)
        {
            Serial.print("Moving from (");
            Serial.print(x1);
            Serial.print(", ");
            Serial.print(y1);
            Serial.print(", ");
            Serial.print(z1);
            Serial.print(") to (");
            Serial.print(x2);
            Serial.print(", ");
            Serial.print(y2);
            Serial.print(", ");
            Serial.print(z2);
            Serial.println(")");

            n = (y2 - y1) / div;
            y_arr[0] = y1;
            for (int i = 1; i < div + 1; i++)
                y_arr[i] = y_arr[i - 1] + n;
            for (int i = 0; i < div + 1; i++)
                x_arr[i] = (x2 - x1) * (y_arr[i] - y1) / (y2 - y1) + x1;
            for (int i = 0; i < div + 1; i++)
                z_arr[i] = (z2 - z1) * (y_arr[i] - y1) / (y2 - y1) + z1;

            for (int i = 0; i < div + 1; i++)
                point(x_arr[i], y_arr[i], z_arr[i]);
        }
        else if (z1 != z2)
        {
            Serial.print("Moving from (");
            Serial.print(x1);
            Serial.print(", ");
            Serial.print(y1);
            Serial.print(", ");
            Serial.print(z1);
            Serial.print(") to (");
            Serial.print(x2);
            Serial.print(", ");
            Serial.print(y2);
            Serial.print(", ");
            Serial.print(z2);
            Serial.println(")");

            n = (z2 - z1) / div;
            z_arr[0] = z1;
            for (int i = 1; i < div + 1; i++)
                z_arr[i] = z_arr[i - 1] + n;
            for (int i = 0; i < div + 1; i++)
                x_arr[i] = (x2 - x1) * (z_arr[i] - z1) / (z2 - z1) + x1;
            for (int i = 0; i < div + 1; i++)
                y_arr[i] = (y2 - y1) * (z_arr[i] - z1) / (z2 - z1) + y1;

            for (int i = 0; i < div + 1; i++)
                point(x_arr[i], y_arr[i], z_arr[i]);
        }
        else
            Serial.println("Points must be difference...");
    }

    void rand_move()
    {
        double x1, y1, z1, x2, y2, z2, d;
        while (true)
        {
            x1 = random(-2000, 2000) / 1000.0;
            y1 = random(0, 2000) / 1000.0;
            z1 = random(0, 2000) / 1000.0;
            d = sqrt(sq(x) + sq(y) + sq(z));
            if (d < 2 && x != 0 && y > 0 && z > 0)
                break;
        }
        while (true)
        {
            x2 = random(-2000, 2000) / 1000.0;
            y2 = random(0, 2000) / 1000.0;
            z2 = random(0, 2000) / 1000.0;
            d = sqrt(sq(x) + sq(y) + sq(z));
            if (d < 2 && x != 0 && y > 0 && z > 0)
                break;
        }
        move(x1, y1, z1, x2, y2, z2);
    }
};

Arm arm; // Creating arm Object.

// set all the initializations in 'setup' function.
void setup()
{
    Serial.begin(9600); // Begin the Serial Monitor.
    arm.attach();       // Servos are attached to Microcontroller.
}

// This will do repeating process.
void loop()
{
    arm.rand_move(); // Arm goes at random move.
    delay(1000);
}
