import numpy as np

#改變格式既有的樣子
#skip_head 把標頭去掉
my_array2 = np.genfromtxt('data2.txt', 
                          skip_header=1,
                          filling_values=0)
print(my_array2)