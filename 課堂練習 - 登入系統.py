#題目4
#解密碼
#使用者輸入帳號與密碼
#輸入對的，顯示"進入系統"
#輸入錯的，顯示"帳號密碼錯誤"
#迴圈次數
#只能輸入錯誤三次
i = 1
ID = 123
PASSWORD = 123

while i < 4:
    #迴圈執行錯誤 即 + 1
    i = i + 1
    ID0 = int(input('請輸入帳號'))
    PASSWORD0 = int(input('請輸入密碼'))
    
    if (ID == ID0) and (PASSWORD == PASSWORD0):
        print('進入系統')
        break
    else:
        print(('密碼錯誤，已輸入錯誤', '%d', '次') % ('i'))
