# 3d Animation of Arm
from matplotlib import projections, pyplot as plt
import numpy as np
import random

ax = plt.axes(projection="3d")
origin_point = (0, 0, 0)


def randompoint_genarator(From=0.5, To=1.9):
    while True:
        x = round(random.uniform(-2, 2), 2)
        y = round(random.uniform(0, 2), 2)
        z = round(random.uniform(0, 2), 2)
        d = np.sqrt(x**2 + y**2 + z**2)
        if From < d < To:
            break
    return (x, y, z)


def point_to_angles(x1=1, y1=1, z1=1, l=1, degree=False):
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


def elbow(x1=1, y1=1, z1=1, l=1):
    d2 = np.sqrt(x1**2 + y1**2 + z1**2)
    if x1 != 0 and y1 != 0 and d2 < 2 * l:
        a0, a1, _ = point_to_angles(x1, y1, z1, l)
        elbow_point = (np.cos(a1) * np.cos(a0), np.cos(a1) * np.sin(a0), np.sin(a1))
        print(f"Elbow Point: {elbow_point}")
        return elbow_point
    else:
        return (0, 0, 0)


def arm(x1=1, y1=1, z1=1, l=1):

    target_point = (x1, y1, z1)
    elbow_point = elbow(target_point[0], target_point[1], target_point[2], l)

    x, y, z = (
        [origin_point[0], elbow_point[0], target_point[0]],
        [origin_point[1], elbow_point[1], target_point[1]],
        [origin_point[2], elbow_point[2], target_point[2]],
    )

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    ax.plot3D([-2, 2], [0, 0], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [-2, 2], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [0, 0], [-2, 2], "--", c="black")

    ax.plot3D(x, y, z, "-og")


def move(p1, p2):
    if p2[0] - p1[0] != 0:
        l = np.linspace(p1[0], p2[0], 20)
        m = (p2[1] - p1[1]) * (l - p1[0]) / (p2[0] - p1[0]) + p1[1]
        n = (p2[2] - p1[2]) * (l - p1[0]) / (p2[0] - p1[0]) + p1[2]

        for i, j, k in zip(l, m, n):
            ax.cla()
            ax.scatter(p2[0], p2[1], p2[2], c="red")
            arm(i, j, k)
            plt.pause(0.01)
    else:
        print("***********  Invalid  **********")


def main(movepath):
    for i in movepath:
        move(i[0], i[1])


points = []

for _ in range(1000):
    points.append(randompoint_genarator())


movepath = []

for i in range(len(points) - 1):
    movepath.append([points[i], points[i + 1]])

main(movepath)
