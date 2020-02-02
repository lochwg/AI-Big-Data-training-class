import numpy as np
"""
x, y, z = np.loadtxt('data1.txt', skiprows=1, unpack=True)

"""
x, y, z = np.loadtxt('data.txt', delimiter = ",",usecols=(0,1,2), unpack=True, dtype=float)

print (y)
#x欄 + y欄
a = x + y
print (a)