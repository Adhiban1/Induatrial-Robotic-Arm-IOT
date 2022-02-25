from matplotlib import pyplot as plt
import math

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


a0, a1, _ = point_to_angles3D()
mpoint = (math.cos(a1) * math.cos(a0), math.cos(a1) * math.sin(a0), math.sin(a1))

ax.plot3D([0, 1], [0, 1], [0, 1], "--", c="blue")
ax.plot3D([0, 1], [0, 0], [0, 0], "--", c="black")
ax.plot3D([1, 1], [0, 1], [0, 0], "--", c="black")
ax.plot3D([0, 1], [0, 1], [0, 0], "--", c="blue")
ax.plot3D([1, 1], [1, 1], [0, 1], "--", c="black")
ax.plot3D(
    [0, math.cos(a1) * math.cos(a0), 1],
    [0, math.cos(a1) * math.sin(a0), 1],
    [0, math.sin(a1), 1],
    "-o",
    c="green",
)
ax.plot3D(
    [0.5, math.cos(a1) * math.cos(a0)],
    [0.5, math.cos(a1) * math.sin(a0)],
    [0.5, math.sin(a1)],
    "--",
    c="black",
)
plt.show()
