import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sqrt(x) + 1 # y = √x + 1

x = np.linspace(0, 4)
y = func(x) # y = f(x)

plt.plot(x, y)
plt.grid()
plt.show()