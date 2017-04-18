import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-12, 12)
y1 = (-1/18) * (x1**2) + 12
plt.plot(x1, y1)

x2 = np.linspace(-4, 4)
y2 = (-1/8) * (x2**2) + 6
plt.plot(x2, y2)

x3 = np.linspace(-12, -4)
y3 = (-1/8) * (x3 + 8)**2 + 6
plt.plot(x3, y3)

x4 = np.linspace(4, 12)
y4 = (-1/8) * (x4 - 8)**2 + 6
plt.plot(x4, y4)

x5 = np.linspace(-4, -0.3)
y5 = 2 * (x5 + 3)**2 - 9
plt.plot(x5, y5)

x6 = np.linspace(-4, 0.2)
y6 = 1.5 * (x6 + 3)**2 - 10
plt.plot(x6, y6)

plt.show()
