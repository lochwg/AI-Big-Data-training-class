x = int(input('請輸入第1個數'))
y = int(input('請輸入第2個數'))
z = int(input('請輸入第2個數'))

#求最大值，使用max當代數做比較
#練習結果：邏輯正確，缺乏代數思維

max(x, y, z)
print (max)

max = x
if y > max:
    max = y
if z > max:
    max = z
print (max)




