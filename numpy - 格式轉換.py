import numpy as np
aa = np.array([(1.9, 1.5, 1.3),(2.9, 2.5, 2.3)], dtype=np.int16)
# ndarray.ndim
print("ndim:{0}".format(aa.ndim))
# ndarry.shape
print("shape:{0}".format(aa.shape))
# ndarry.size
print("size:{0}".format(aa.size))
# ndarry.dtpye
print("dtype:{0}".format(aa.dtype))
# ndarry.itemsize
print("itemsize:{0}".format(aa.itemsize))
# ndarry.data
print("data:{0}".format(aa.data))


#大數據可能處理影片、圖片、數字，要告訴電腦哪種datatype可以使用

#老師辛苦了！