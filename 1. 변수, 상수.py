# 다차원 배열을 다루는 데 사용되는 핵심 라이브러리
# 효율적인 배열 연산을 수행할 수 있으며,
# 수학적 함수와 메서드를 제공하여 데이터 처리 및 분석 용이
import numpy as np
# 파이썬에서 그래프를 그릴 때 주로 사용되는 라이브러리
import matplotlib.pyplot as plt

a = 2.5  # a : 상수
x = np.linspace(-1, 1)  # x : 변수 -1부터 1의 범위
y = a * x  # y : 변수, 즉 y = ax 구현

# x, y 값을 받아 그래프 생성
plt.plot(x, y)
plt.xlabel("x", size=22)  # x축의 라벨
plt.ylabel("y", size=22)  # y축의 라벨
plt.grid()  # 표에 그리드(줄) 표시
plt.show()  # 그래프 확인
