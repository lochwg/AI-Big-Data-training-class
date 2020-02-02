import os
def menu():
    os.system("cls")
    print("帳號、密碼管理系統")
    print("-------------------")
    print("1. 輸入帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("0. 結  束  程  式")
    print("-------------------")

def input_data():
    while True:
        #帳號
        name = input("請輸入帳號(Enter==>停止輸入)")
        if name == "": break
        sqlstr = "select * from password where name='{}'".format(name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if not row == None:  
            print("{}帳號已存在!".format(name))
            continue
        #密碼
        password = input("請輸入密碼: ")
        sqlstr = "insert into password values('{}','{}');".format(name, password)
        conn.execute(sqlstr)
        conn.commit()
        #資料庫使用完畢 關閉資料庫
        print("{}已被儲存完畢".format(name))

#直接把sql寫入程式讀取當中

    
def disp_data():
    cursor = conn.execute('select * from password')
    print("帳號\t密碼")
    print("=================")
    for row in cursor:
        print("{}\t{}".format(row[0],row[1]))
    input("按任意鑑返回主選單")
        
## 主畫面開始
    
import sqlite3

conn = sqlite3.connect('passwords.sqlite')
cursor = conn.cursor()

#建立database
sqlstr = 'CREATE TABLE IF NOT EXISTS password \
("name" TEXT PRIMARY KEY NOT NULL, "pass" TEXT)'
cursor.execute(sqlstr)

while True:
    menu()
    choice = int(input("請輸入您的選擇: "))
    print()
    if choice ==1:
        input_data()
    elif choice ==2:
        disp_data()
    else:
        break

print("程式執行完畢！")

