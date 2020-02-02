#panda多使用於excel生成、繪圖

import pandas as pd
import numpy as np


#reshape 10x10的矩陣

data = np.arange(1,101).reshape((10, 10))
#DataFrame格式化
data_df = pd.DataFrame(data)

data_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#index 索引
data_df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


#ExcelWriter 例如公家機關多是CSV的檔案

writer = pd.ExcelWriter('Save_Excel2.xlsx')
#data_df 把資料格式化 避免錯誤
#float_format 浮點數
#data_df 屬於自設代號
data_df.to_excel(writer,'page_1', float_format='%.5f')
writer.save()