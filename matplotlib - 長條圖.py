import matplotlib.pyplot as vv
import pandas as pd

csv_data = pd.read_csv(r'1072.csv', engine = 'python')
x = csv_data.head(15)
print(x)

pp = csv_data[['C1', 'D1']].head(5)
print (pp)

vv.plot(x)
vv.show