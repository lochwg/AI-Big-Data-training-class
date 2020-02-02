#老師的示範
import numpy as np
import pandas as pd

data = np.loadtxt('data4.txt', skiprows = 1, unpack = True)
data1 = np.loadtxt('data4.txt', usecols = (0, 1, 2, 3, 4), dtype = str)

print (data)
print (data1)
data_1 = pd.DataFrame(data1)
data_2 = pd.DataFrame(data)
print (data_2)

#[index, colums]
#tranpose 把
#{} 會變成隨機數 

writer = pd.ExcelWriter('SaveExcel1.xlsx')
data_2.to_excel('SaveExcel2.xlsx')
writer.save() 


#usecol = usecolum 使用欄