
import pandas as pd
# r 讀取
csv_data = pd.read_csv(r'學生體重平均值(6歲-15歲).csv', engine = 'python')
print(csv_data.head(15))
N = 5
csv_batch_data = csv_data.tail(N) 
#取後面5條資料
print(csv_batch_data.shape)
