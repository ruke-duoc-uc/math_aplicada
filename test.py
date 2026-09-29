import numpy as np
import matplotlib.pyplot as plt

def s(x):
    return -1.6*x**2+1.3*x+141.3
def r(x):
    return 1.4*x**2-5.6*x+12.6

t = np.linspace(-6,8, 200)
y = s(t)

t2 = np.linspace(-6, 8, 200)
y2 = r(t2)

plt.plot(t, y, color="blue", linewidth=2, label="f(t)")
plt.plot(t2, y2, color="blue", linewidth=2, label="f(t)")
for i in range(-10,10):
    print(f"Numero {i}")
    print(f"s(i){s(i)}")
    print(f"r(i){r(i)}")
plt.show()
