from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

ax = plt.axes(projection='3d')


def point_to_angles3D(point=(1, 1, 1), l=1):  # 3D point, length -> 3 angles
    if point[0] == 0 and point[1] == 0:
        d1 = np.sqrt(0.01**2 + 0.01**2)
    else:
        d1 = np.sqrt(point[0] ** 2 + point[1] ** 2)
    d2 = np.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)
    if d2 < 2 * l:
        a0 = np.arccos(point[0] / d1)
        a1 = np.arccos(d1 / d2) + np.arccos(d2 / (2 * l))
        a2 = np.pi - 2 * np.arccos(d2 / (2 * l))

        return (a0, a1, a2)
    else:
        print("********** Out Of Range ***********")

        return (0, 0, 0)  # Default Position


def point_to_graph3D(x1, y1, z1):
    point = (x1, y1, z1)
    a0, a1, _ = point_to_angles3D(point, 1)
    mpoint = (np.cos(a1) * np.cos(a0), np.cos(a1) * np.sin(a0), np.sin(a1))
    x = [0, mpoint[0], point[0]]
    y = [0, mpoint[1], point[1]]
    z = [0, mpoint[2], point[2]]
    ax.plot3D(x, y, z, "-o")


def randompoint_genarator(From=1.5, To=2):
    while True:
        x = round(random.uniform(-2, 2), 2)
        y = round(random.uniform(0, 2), 2)
        z = round(random.uniform(0, 2), 2)
        d = np.sqrt(x**2 + y**2 + z**2)
        if From < d < To:
            break
    return (x, y, z)


while True:
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    x, y, z = randompoint_genarator()
    ax.plot3D([-2, 2], [0, 0], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [-2, 2], [0, 0], "--", c="black")
    ax.plot3D([0, 0], [0, 0], [-2, 2], "--", c="black")
    point_to_graph3D(x, y, z)
    plt.pause(0.5)
