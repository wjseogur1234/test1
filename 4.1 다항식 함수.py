import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 4*x**3 + 2*x**2 + x + 3

x = np.linspace(-2, 2)
y = func(x)

plt.plot(x, y)
plt.grid()
plt.show()