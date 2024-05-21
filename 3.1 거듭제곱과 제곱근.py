import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x) # x의 양(+)의 제곱근, x**(1/2)로도 같음

x = np.linspace(0, 9)
y = f(x)

plt.plot(x, y)
plt.grid()
plt.show()