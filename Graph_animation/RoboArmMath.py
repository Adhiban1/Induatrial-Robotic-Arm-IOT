from matplotlib import pyplot as plt
import numpy as np

plt.xlim(-3,3)
plt.ylim(-3,3)

def line(p0: tuple, p1: tuple): # Line function
    plt.plot([p0[0],p1[0]],[p0[1],p1[1]], '-og')

def arm(angle1=135, angle2=45): # angles in Degree
    line(
        (0,0),
        (np.cos(angle1*2*np.pi/360), np.sin(angle1*2*np.pi/360))
        )
    line(
        (np.cos(angle1*2*np.pi/360), np.sin(angle1*2*np.pi/360)),
        (np.cos(angle2*2*np.pi/360)+np.cos(angle1*2*np.pi/360), np.sin(angle2*2*np.pi/360)+np.sin(angle1*2*np.pi/360))
    )

########################

d = 1.5
# a1 = 2*np.pi/360*np.arctan(2*(np.sqrt(1-((d**2)/4)))/d)
a1 = np.arctan(2*(np.sqrt(1-((d**2)/4)))/d) * 180/(np.pi)
a2 = -a1
print(a1,a2)
########################

arm(a1,a2)

plt.plot([-3,3],[0,0], '--')
plt.grid(True)
plt.show()

