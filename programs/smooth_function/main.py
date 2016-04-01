import scipy as sp
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return sp.sin(x / 5) * sp.exp(x / 10) + 5 * sp.exp(-x / 2)

def h(x):
    return int(f(x))

def h1(x):
    return int(sp.sin(x / 5) * sp.exp(x / 10) + 5 * sp.exp(-x / 2))

a = scipy.optimize.minimize(f, 30, method='BFGS')
b = scipy.optimize.differential_evolution(f, [(1, 30)])
c = scipy.optimize.minimize(h, 30, method='BFGS')
d = scipy.optimize.differential_evolution(h, [(1, 30)])

print(a, b, c, d)

x = np.linspace(1, 30, 200)

y = f(x)
y_int  = h1(x)

#plt.plot(x, y)
#plt.show()
