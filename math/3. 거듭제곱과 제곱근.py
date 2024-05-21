import numpy as np
import matplotlib.pyplot as plt

# 주석키 안 먹을때 Ctrl + Shift 눌러서 Microsoft 입력기로 바꾸기

def func(x):
    a = 3
    return x ** a # x의 거듭제곱

x = np.linspace(0, 2)
y = func(x) # y = f(x)

plt.plot(x,y)
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()

