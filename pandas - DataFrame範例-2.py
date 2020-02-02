import pandas as pd
#[]內多一個()會有不同結果
datas = [[66,70,35,58],[90,65,77,89],[45,80,63,51],\
         [73,70,88,90],[55,67,82,73],[80,67,62,55]]
indexs = ['Kyle','John','Eric','Mike','Rick','Emma']
columns = ['國文','英文','數學','自然']

#index沒有加s為pd預設
df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)
