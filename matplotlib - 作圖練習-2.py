import matplotlib.pyplot as plt
import numpy as np

a = np.array([5, 7, 81, 42, 41, 43, 92, 
              91, 3, 40, 15, 2, 39, 21, 
              80, 81, 30, 42, 51, 43, 30, 
              14, 16, 37, 72, 94, 62, 71])

#sin cos的角度
#a = np.linspace(0, 2 * np.pi, 50)
print (a)
b = np.cos(a)
print (b)
plt.plot (a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'm^')
#mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'm^')
plt.show()
