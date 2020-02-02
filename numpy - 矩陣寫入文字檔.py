import numpy as np
x = np.arange(5, 5, 5)
np.savetxt('test2.out', x, delimiter = ",",fmt = "%s, %s")
