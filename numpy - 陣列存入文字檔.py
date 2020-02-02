import numpy as np
x = np.arange(10) #自行產生data
np.savetxt('test2.out', x, delimiter = ",")
print (x)