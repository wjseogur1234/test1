import numpy as np
import matplotlib.pyplot as plt

def tan(x):
    return np.tan(x)

x = np.linspace(-1.3, 1.3)
y_tan = tan(x)

plt.plot(x, y_tan, label="tan")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()

plt.show()
