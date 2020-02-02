import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2 * np.pi, 50)
print (a)
#畫線條用
b = np.cos(a)
print (b)

#繪圖做線
plt.plot (a,b)
mask = b >= 0
#bo是函點 

plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
#分開區間
plt.plot(a[mask], b[mask], 'go')
plt.show()

#show是把圖表跑出來
#line15之後