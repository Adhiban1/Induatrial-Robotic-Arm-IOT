#include <iostream>
#include <math.h>
using namespace std;

void point_to_servoMove(double x = 1, double y = 1, double z = 1, double l = 1)
{
    double d1, d2, a0, a1, a2, a4;
    if (x == 0 && y == 0)
    {
        d1 = sqrt(pow(0.001, 2) + pow(0.001, 2));
    }
    else
    {
        d1 = sqrt(pow(x, 2) + pow(y, 2));
    }
    d2 = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    if (d2 < 2 * l)
    {
        a0 = acos(x / d1);
        a1 = acos(d1 / d2) + acos(d2 / (2 * l));
        a2 = M_PI - 2 * acos(d2 / (2 * l));
        a4 = (3 * M_PI / 2) - a1 - a2;
    }
    else
    {
        a0 = 90;
        a1 = 150;
        a2 = 60;
        a4 = 45;
    }
};

int main()
{
    cout << "Point to Servo Movement.";
    return 0;
}