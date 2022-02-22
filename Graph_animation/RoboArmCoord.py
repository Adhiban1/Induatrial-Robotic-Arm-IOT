from matplotlib import pyplot as plt
import numpy as np



def arm(x,y):
    target = (x,y)
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    distance = np.sqrt(target[0]**2+target[1]**2)
    if distance < 2 and x > 0 and y > 0:
        a1 = np.arctan(target[1]/target[0]) + \
            np.arctan(np.sqrt((4-target[0]**2-target[1]**2)/(target[0]**2+target[1]**2)))

        x = [0, np.cos(a1), target[0]]
        y = [0, np.sin(a1), target[1]]

        plt.plot(x,y, '-o')
        plt.grid(True)
        plt.plot([-3,3],[0,0], '--')
        plt.show()
    else:
        print('Out of Range')

arm(1,0.001)