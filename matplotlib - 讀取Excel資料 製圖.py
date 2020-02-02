import matplotlib.pyplot as bb
import pandas as pd
csv_data = pd.read_csv(r'學生體重平均值(6歲-15歲).csv', engine = 'python')
x = csv_data.head(15)

bb.plot(x)
bb.title("AAAA")
bb.show