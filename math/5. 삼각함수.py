import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(x)

def cos(x):
    return  np.cos(x)

x = np.linspace(-np.pi, np.pi)
y_sin = sin(x)
y_cos = cos(x)

plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, label="cos")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()

plt.show()
