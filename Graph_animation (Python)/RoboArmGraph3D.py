from matplotlib import pyplot as plt
import math
import numpy as np
import random

fig = plt.figure()
ax = plt.axes(projection="3d")


def point_to_angles3D(point=(1, 1, 1), l=1):  # 3D point, length -> 3 angles
    if point[0] == 0 and point[1] == 0:
        d1 = math.sqrt(0.01**2 + 0.01**2)
    else:
        d1 = math.sqrt(point[0] ** 2 + point[1] ** 2)
    d2 = math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)
    if d2 < 2 * l:
        a0 = math.acos(point[0] / d1)
        a1 = math.acos(d1 / d2) + math.acos(d2 / (2 * l))
        a2 = math.pi - 2 * math.acos(d2 / (2 * l))

        return (a0, a1, a2)
    else:
        print("********** Out Of Range ***********")

        return (0, 0, 0)  # Default Position


# def move(point1, point2):
#     x1, y1, z1 = point1
#     x2, y2, z2 = point2
#     x = np.linspace(x1, x2, 20)
#     y = (x - x1) * (y2 - y1) / (x2 - x1) + y1
#     z = (x - x1) * (z2 - z1) / (x2 - x1) + z1

#     for i in zip(x, y, z):
#         ax.cla()
#         a0, a1, a2 = point_to_angles3D(i, 1)
#         mpoint = (
#             math.cos(a1) * math.cos(a0),
#             math.cos(a1) * math.sin(a0),
#             math.sin(a1),
#         )
#         l = [0, mpoint[0], i[0]]
#         m = [0, mpoint[1], i[1]]
#         n = [0, mpoint[2], i[2]]
#         ax.set_title(str(i))
#         ax.plot3D(l, m, n, "-o", c="green")
#         plt.pause(1)


def point_to_graph3D(x1, y1, z1):
    point = (x1, y1, z1)
    a0, a1, _ = point_to_angles3D(point, 1)
    mpoint = (math.cos(a1) * math.cos(a0), math.cos(a1) * math.sin(a0), math.sin(a1))
    x = [0, mpoint[0], point[0]]
    y = [0, mpoint[1], point[1]]
    z = [0, mpoint[2], point[2]]
    ax.plot3D(x, y, z, "-o")


def randompoint_genarator(From=1.5, To=2):
    while True:
        x = round(random.uniform(-2, 2), 2)
        y = round(random.uniform(0, 2), 2)
        z = round(random.uniform(0, 2), 2)
        d = math.sqrt(x**2 + y**2 + z**2)
        if From < d < To:
            break
    return (x, y, z)


def multiple_arms(n):
    for i in range(n):
        x1, y1, z1 = randompoint_genarator()
        point_to_graph3D(x1, y1, z1)


# point = (1, 1, 1)

# a0, a1, a2 = point_to_angles3D(point, 1)

# mpoint = (math.cos(a1) * math.cos(a0), math.cos(a1) * math.sin(a0), math.sin(a1))

# x = [0, mpoint[0], point[0]]
# y = [0, mpoint[1], point[1]]
# z = [0, mpoint[2], point[2]]


ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

ax.plot3D([-2, 2], [0, 0], [0, 0], "--", c="black")
ax.plot3D([0, 0], [-2, 2], [0, 0], "--", c="black")
ax.plot3D([0, 0], [0, 0], [-2, 2], "--", c="black")

multiple_arms(100)
# point_to_graph3D(1, 1, 1)
plt.show()
