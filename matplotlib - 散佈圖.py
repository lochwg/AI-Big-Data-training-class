import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('YouBike.csv')
xData = df[df.tot == 50].iloc[:,6] #緯度
yData = df[df.tot == 50].iloc[:,7] #經度

print (xData)

plt.scatter(xData, yData)
plt.rcParams['font.sans-'] = ['times-newroman']
plt.rcParams['axes.unicode_minus'] = False #用來正常顯示負號
plt.xlabel("latitude", fontsize = 14) 
plt.ylabel("longitude", fontsize = 14)
plt.show
