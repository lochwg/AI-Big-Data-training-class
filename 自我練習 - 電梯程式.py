
#自我練習-3
#大樓有兩座電梯，如何使電梯使用效率達到最佳化，減少電力的使用？
#大樓提供兩台電梯(elevator)，隨機出現在1至13樓，取亂數E1跟E2

import random
E1 = random.randint(1,13)
E2 = random.randint(1,13)

#兩台電梯目前分別在幾樓？
Data1 = {'stre1': '目前一號電梯位於', 'vare1': E1, 'stre12': '樓' }
msg1 = '%(stre1)s %(vare1)s %(stre12)s' % Data1
Data2 = {'stre2': '目前二號電梯位於', 'vare2': E2, 'stre22': '樓' }
msg2 = '%(stre2)s %(vare2)s %(stre22)s' % Data2
print (msg1)
print (msg2)
#簡化做法
msg3 ='目前一號電梯位於 {0} 樓\n目前二號電梯位於 {1} 樓' .format(E1, E2)
print (msg3)
#請問你現在在幾樓？
C = int(input('請告訴我您在幾樓？'))
#最近的電梯移動到當前樓，比較E1、E2與當前樓層的距離，越近者優先
if abs(E1 - C) < abs(E2 - C):
    print ('請搭1號電梯')
else:
    print ('請搭2號電梯')
    
#謝謝賴老師，辛苦了～
