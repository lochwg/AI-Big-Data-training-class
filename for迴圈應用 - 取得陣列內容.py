#for(起始值;終值;遞增、遞減值)
#[]陣列符號
#沒有遞增遞減值 = 代表每次都+1 
#for不能與print齊平，必須往內縮，代表從屬關係
#記得陣列排序 從0開始，如果要找中位數，電腦會判斷，從0開始

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
#guin lanages 代表陣列的長度
#x = 陣列長度 0, 1, 2, 3

#range是陣列長度
sum = 0
i = 1
for i in range(1, 11):
#range初始值1 與括弧11 
#值必須小於11 系統自動判斷  i < 11 => 1到10
    sum = sum+i
#sum +=i == sum = sum + i
#sum值，從第21行
#縮排，是指包含在裡面
    print (i)
    print (sum)
    



