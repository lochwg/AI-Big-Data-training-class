import numpy as np
import pandas as pd

#出現CP950 多為編碼方(utf-8、ASCII)式的錯誤
#國, 英, 數, 自, 社 = np.loadtxt('test.txt', delimiter = ",",usecols=(0,1,2,3,4), unpack=True)

Data =  np.loadtxt('test.txt', skiprows = 1, unpack = True)
print (Data)

data_df = pd.DataFrame (Data)
print(data_df)

#pandas 不用允許data_df.colums = ['科目', '小明', '小花', '小新']
#Pandas doesn't allow columns to be created via a new attribute name
data_df.index = ['國文', '英文', '數學', '自然', '社會']

writer = pd.ExcelWriter('成績單.xlsx')
data_df.to_excel(writer,'page_1', float_format='%.5f')
writer.save()

#為什麼要更改欄位名稱，因為有可能是根據學號排序，會看不懂，因此要將學號改成學生姓名