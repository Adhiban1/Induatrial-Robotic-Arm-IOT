#include <iostream>
#include <math.h>
using namespace std;

double *point_to_angles3D(double x = 1, double y = 1, double z = 1, double l = 1)
{
    double d1, d2, a0, a1, a2, a4;
    double *angles = new double[4];
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
        angles[0] = a0 * (180 / M_PI);
        angles[1] = a1 * (180 / M_PI);
        angles[2] = a2 * (180 / M_PI);
        angles[3] = a4 * (180 / M_PI);
    }
    else
    {
        angles[0] = 90;
        angles[1] = 150;
        angles[2] = 60;
        angles[3] = 45;
    }
    return angles;
};

int main()
{
    double *angles_0 = point_to_angles3D();
    double angles[] = {*angles_0, *(angles_0 + 1), *(angles_0 + 2), *(angles_0 + 3)};

    cout << "angle0: " << angles[0] << endl;
    cout << "angle1: " << angles[1] << endl;
    cout << "angle2: " << angles[2] << endl;
    cout << "angle4: " << angles[3] << endl;

    return 0;
}