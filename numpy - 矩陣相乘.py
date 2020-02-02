import numpy as np
l1 = np.arange(5)
l2, l3 = l1*2, l1*3
print (l1)
print (l3)
np.savetxt('002.txt',(l1,l2,l3))
np.loadtxt('002.txt')