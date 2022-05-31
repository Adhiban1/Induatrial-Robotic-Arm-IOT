import numpy as np
import math
from matplotlib import pyplot as plt

x = np.linspace(-1, 1, 100)
y = list(map(lambda i: (180 / math.pi) * math.acos(i), x))
y1 = list(map(lambda i: (180 / math.pi) * math.asin(i), x))
y2 = list(map(lambda i: (180 / math.pi) * math.atan(i), x))
plt.plot(x, y, label="acos")
plt.plot(x, y1, label="asin")
plt.plot(x, y2, label="atan")
plt.plot([-1, 1], [0, 0], "--", c="black")
plt.plot([0, 0], [-100, 200], "--", c="black")
plt.legend()
print(
    f"""x range: {min(x)} to {max(x)}
cos range: {min(y)} to {max(y)}
sin range: {min(y1)} to {max(y1)}
tan range: {min(y2)} to {max(y2)}"""
)
plt.show()
