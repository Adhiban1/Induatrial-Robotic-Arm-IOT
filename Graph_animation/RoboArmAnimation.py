import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

a = np.linspace(0, np.pi / 2, 100)
c = 2 * np.cos(a)
s = 2 * np.sin(a)


def arm(x, y):
    target = (x, y)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    distance = np.sqrt(target[0] ** 2 + target[1] ** 2)
    if distance < 2 and x > 0 and y > 0:
        a1 = np.arctan(target[1] / target[0]) + np.arctan(
            np.sqrt(
                (4 - target[0] ** 2 - target[1] ** 2)
                / (target[0] ** 2 + target[1] ** 2)
            )
        )

        x = [0, np.cos(a1), target[0]]
        y = [0, np.sin(a1), target[1]]

        ax.plot(x, y, "-o")
        # ax.grid(True)
        ax.plot([-3, 3], [0, 0], "--")
        ax.plot(c, s, "r")
        ax.plot([0, 0], [0, 2], "r")
        # plt.show()
    else:
        print("********** Out of Range **********")


def move(p1, p2):

    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]

    if (x[1] - x[0]) != 0:
        l = np.linspace(x[0], x[1], 20)
        m = (l - x[0]) * (y[1] - y[0]) / (x[1] - x[0]) + y[0]

        for i, j in zip(l, m):
            ax.cla()
            ax.scatter(p2[0], p2[1], c="green")
            arm(i, j)
            # ax.set_title("frame {}".format(i)
            # Note that using time.sleep does *not* work here!
            plt.pause(0.01)
    else:
        print("***********  Invalid  **********")


def main(movepath):
    for i in movepath:
        move(i[0], i[1])


points = [
    (0.066, 1.909),
    (0.285, 0.11),
    (0.692, 1.779),
    (0.896, 0.11),
    (1.299, 1.448),
    (1.471, 0.196),
    (1.863, 0.571),
    (0.066, 1.909),
]

movepath = []

for i in range(len(points) - 1):
    movepath.append([points[i], points[i + 1]])

while True:
    main(movepath)
# arm(1, 1)
# plt.show()
