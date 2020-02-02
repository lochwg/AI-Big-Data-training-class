

import pandas as pd

datas = [[66,70,35,58],[90,65,77,89],[45,80,63,51],\
         [73,70,88,90],[55,67,82,73],[80,67,62,55]]
indexs = ['Kyle','John','Eric','Mike','Rick','Emma']
columns = ['國文','英文','數學','自然']

df = pd.DataFrame(datas, columns=columns, index=indexs)

print('移除數學及自然的成績')
df_1 = df.drop(["數學","自然"], axis = 1)
print(df_1)

print('移除Kyle到Eric的成績')
df_2 = df.drop(df.index[0:2])
print(df_2)

print('移除英文到數學的成績')
df_3 = df.drop(df.columns[1:3], axis = 1)
print(df_3)



