A=100
# > < >= <= !=不等於
#判斷成績
if A < 60:
    print("不及格")
else:
    print("及格")
#國文成績80，數學成績90，英文成績60，計算加總、平均數
x = 80
y = 90
z = 60
sum = x + y + z
avg = int(sum / 3)
#程式規則：排序，第一個是0，每個框只能丟一個值
# \n 換行，容易打錯成 /n
msg = '國文{0}分\n英文{1}分\n數學{2}分\n總分{3}分\n平均{4}分' .format(x, y, z, sum, avg)
print (msg)

#判斷 if... else...
if x >= 60:
    print("國文及格")
else:
    print("國文不及格")
    
if y >= 60:
    print("數學及格")
else:
    print("數學不及格")

if z >= 60:
    print("英文及格")
else:
    print("英文不及格")
    
# 多個條件如何處理 if... elif... else...
if x >= 80:
    print("優質")
elif x >= 70:
    print("普通")
elif x >= 60:
    print("及格")
elif x >= 50:
    print("重考")
#最後一個要輸入正確 < 50-1個數
elif x < 49:
    print("重修")


print(sum)
print(avg)
print(msg)