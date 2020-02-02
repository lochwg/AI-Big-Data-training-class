import numpy as np

#先把a做5*5的矩陣
#a就是1至25塞入5*5的矩陣
a = np.arange(25)
a = a.reshape((5, 5))
print (a)

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print (b)
print ("------------------------------")
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print ("------------------------------")

