# 3d Animation of Arm
from matplotlib import pyplot as plt
import numpy as np
import random

ax = plt.axes(projection="3d")  # Creating 3D Axes.
origin_point = (0, 0, 0)  # Arm is placed at Origin.
segments = 20  # (More Segment) -> (Smooth move, but slow move).


def randompoint_genarator(From=0.5, To=1.9):  # This function gives valid Random Point.
    while True:
        x = round(random.uniform(-2, 2), 2)
        y = round(random.uniform(0, 2), 2)
        z = round(random.uniform(0, 2), 2)
        d = np.sqrt(x**2 + y**2 + z**2)
        if From < d < To:
            break
    return (x, y, z)


def point_to_angles(x1=1, y1=1, z1=1, l=1, degree=False):  # Point to a0,a1,a2 angles.
    d1 = np.sqrt(x1**2 + y1**2)
    if d1 == 0:
        d1 = 0.0001
    a0 = np.arccos(x1 / d1)
    d2 = np.sqrt(x1**2 + y1**2 + z1**2)

    if d2 < 2 * l:
        m = d2 / 2
        t1 = np.arccos(m / l)
        t2 = np.arccos(d1 / d2)
        a1 = t1 + t2
        a2 = np.pi - 2 * t1
        if degree:
            a0 = a0 * (180 / np.pi)
            a1 = a1 * (180 / np.pi)
            a2 = a2 * (180 / np.pi)

        print("Angle0: {0:2.2f}, Angle1: {1:2.2f}, Angle2: {1:2.2f}".format(a0, a1, a2))
        return (a0, a1, a2)

    else:
        print("-----------Out of range-----------")
        return (None, None, None)


def elbow(x1=1, y1=1, z1=1, l=1):  # This gives Elbow point of Arm.
    d2 = np.sqrt(x1**2 + y1**2 + z1**2)
    if x1 != 0 and y1 != 0 and d2 < 2 * l:
        a0, a1, _ = point_to_angles(x1, y1, z1, l)
        elbow_point = (np.cos(a1) * np.cos(a0), np.cos(a1) * np.sin(a0), np.sin(a1))
        print(f"Elbow Point: {elbow_point}")
        return elbow_point
    else:
        return (0, 0, 0)


def arm(x1=1, y1=1, z1=1, l=1):  # Point -> Arm Graph for that particulat point only.

    target_point = (x1, y1, z1)
    elbow_point = elbow(
        target_point[0], target_point[1], target_point[2], l
    )  # Calling elbow function.

    x, y, z = (
        [origin_point[0], elbow_point[0], target_point[0]],
        [origin_point[1], elbow_point[1], target_point[1]],
        [origin_point[2], elbow_point[2], target_point[2]],
    )

    ax.set_xlim(-2 * l, 2 * l)
    ax.set_ylim(-2 * l, 2 * l)
    ax.set_zlim(-2 * l, 2 * l)

    ax.plot3D([-2 * l, 2 * l], [0, 0], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [-2 * l, 2 * l], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [0, 0], [-2 * l, 2 * l], "--", c="black")
    ax.plot3D(x, y, z, "-og")  # Arm Graph.


def move(p1, p2):  # This function moves Arm from One point(p1) to Another point(p2).
    if p2[0] - p1[0] != 0:  # Condition for valid Move.
        l = np.linspace(p1[0], p2[0], segments)
        m = (p2[1] - p1[1]) * (l - p1[0]) / (p2[0] - p1[0]) + p1[1]
        n = (p2[2] - p1[2]) * (l - p1[0]) / (p2[0] - p1[0]) + p1[2]

        for i, j, k in zip(l, m, n):
            ax.cla()  # Clears the Axes.
            ax.scatter(p2[0], p2[1], p2[2], c="red")  # Target point in plot.
            arm(i, j, k)  # Arm Function is used.
            plt.pause(0.01)  # sleep does not work here. Use pause only.
    else:
        print("***********  Invalid  **********")


def main(movepath):  # This fuction converts point to movement of Arm.
    for i in movepath:
        move(i[0], i[1])


points = []  # Creating Empty list.
n = 1000  # number of point needed.
for _ in range(n):
    points.append(randompoint_genarator())  # random points are stored in 'points'.


movepath = []  # Creating Empty list.

for i in range(len(points) - 1):  # Starting and Ending points in 'movepath'.
    movepath.append([points[i], points[i + 1]])

main(movepath)  # Calling main Function.
