
import pandas as pd

datas = [[66,70,35,58],[90,65,77,89],[45,80,63,51],\
         [73,70,88,90],[55,67,82,73],[80,67,62,55]]
indexs = ['Kyle','John','Eric','Mike','Rick','Emma']
columns = ['國文','英文','數學','自然']

df = pd.DataFrame(datas, columns=columns, index=indexs)

print('資料排序，按照英文分數')
#ascending(遞增) = Ture(由上到下，越來越大) False(由上到下，越來越小)
df_1 = df.sort_values(by="英文", ascending=True)
print(df_1)

print('按照列標題進行遞增排序')
df_2 = df.sort_index(axis=0)
print(df_2)

