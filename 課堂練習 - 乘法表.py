
i = 1
j = 1

#外層的for 完成"列"
for i in range(1,10):
#內層的for 完成"欄"
    for j in range(1,10):
        s = i * j
        print (('%d * %d = % d') % (i, j, s))
        
    
a=0    
for i in range(1,10):
    a = a + 1
    s = i * a
    if a > 10:
        break
    print (('%d * %d = % d') % (i, a, s))