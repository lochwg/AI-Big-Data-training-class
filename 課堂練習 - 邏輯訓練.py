
#a, b, c是給你做選擇的 只適用於函式內 對外並不適用 '行話'
#例如便當店 客人買'排骨飯加飯' 便當店內會說'徘+飯' 

#先從最大的開始定義

def sum(a, b, c):
    
#迴圈一 判斷是否為三角形
  if a < b + c and b < a + c and c < a + b:
      
     if a == b == c:
        print('等邊三角形')
     elif a == b or b == c or c == a:
         if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
            print('等腰直角三角形')
         else: 
            print('等腰三角形')
     elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
        print('直角三角形')
     else:
        print('三角形')
  else:
      print('這不是個三角形')

x = int(input("請輸入x:"))
y = int(input("請輸入y:"))
z = int(input("請輸入z:"))
print(sum(x, y, z))