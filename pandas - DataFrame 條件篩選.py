
import pandas as pd

datas = [[66,70,35,58],[90,65,77,89],[45,80,63,51],\
         [73,70,88,90],[55,67,82,73],[80,67,62,55]]
indexs = ['Kyle','John','Eric','Mike','Rick','Emma']
columns = ['國文','英文','數學','自然']

df = pd.DataFrame(datas, columns=columns, index=indexs)

mask_1 = df.數學 >= 80
mask_2 = df.英文 >= 50

# =============================================================================
# print(df.loc[mask_1].head())
# =============================================================================
print(df.loc[mask_1].head())&(df.loc[mask_2].head())
