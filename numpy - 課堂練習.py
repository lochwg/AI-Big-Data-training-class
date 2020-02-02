
import numpy as np

a = np.array([5, 7, 81, 42, 41, 43, 92, 
              91, 3, 40, 15, 2, 39, 21, 
              80, 81, 30, 42, 51, 43, 30, 
              14, 16, 37, 72, 94, 62, 71])

a = a.reshape ((4,7))

#reshape (index, colums)

print(a)
print(a.sum())
print(a.min())
print(a.max())

a = np.unique(a)
print(a)

#unique 沒有重覆值，還能幫你排序 
#複習
