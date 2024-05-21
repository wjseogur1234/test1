import  numpy as np
import matplotlib.pyplot as plt

def func(x):
    return  3*x**2 + 2*x + 1

x = np.linspace(-2, 2)
y = func(x)

plt.plot(x, y)
plt.grid()
plt.show()