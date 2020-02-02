import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('不動產實價登錄資訊-買賣案件.csv')
xData = df[df.district == '林口區' ].iloc[:,2] 
yData = df[df.district == '林口區' ].iloc[:,21] 

print (xData)
print (yData)

plt.bar(xData, yData)
plt.scatter(xData, yData)
plt.rcParams['font.sans-serif'] = ['times-newroman']
plt.rcParams['axes.unicode_minus'] = False #用來正常顯示負號
plt.xlabel("Location", fontsize = 14) 
plt.ylabel("Price", fontsize = 14)
plt.title("LIN-CO District", fontsize = 22)
plt.show()


