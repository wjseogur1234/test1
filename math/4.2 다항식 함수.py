import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3 - 2*x**2 - 3*x + 4 # y = x^3 - 2x^2 - 3x + 4

x = np.linspace(-2, 2)
y = func(x)

plt.plot(x, y)
plt.grid()
plt.show()