import scipy
import math as m
import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(1, 15, 200)
y = scipy.sin(x / 5) * scipy.exp(x / 10) + 5 * scipy.exp(-2 * x / 2)
x_t = np.array([1, 4, 6, 10, 12, 15])
y_t = scipy.sin(x_t / 5) * scipy.exp(x_t / 10) + 5 * scipy.exp(- 2 * x_t / 2)
plt.plot(x, y)
b = np.array([y_t[0], y_t[1], y_t[2], y_t[3], y_t[4], y_t[5]])
A = np.array([[1, 1, 1, 1, 1, 1], [1, 4, 16, 4**3, 4**4, 4**5], [1, 6, 36, 6**3, 6**4, 6**5], [1, 10, 100, 1000, 10**4, 10**5],
              [1, 12, 144, 12**3, 12**4, 12**5], [1, 15, 225, 15**3, 15**4, 15**5]])
solutions = np.linalg.solve(A, b)
print(solutions)
y_aprox = solutions[0] + solutions[1] * x + solutions[2] * (x ** 2) + solutions[3] * (x ** 3) + solutions[4] * (x**4) + solutions[5] * (x**5)
plt.plot(x, y_aprox)
plt.show()
time.sleep(60)