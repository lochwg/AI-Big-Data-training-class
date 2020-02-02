import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor() #建立cursor物件

sqlstr = [(2, '07-88888'),(3, '04-55555'),(4, '02-55555')]

cursor.executemany('insert into table01 values(?,?);', sqlstr);
print('資料筆數', cursor.rowcount)

conn.commit() #主動更新
conn.close() #關閉資料庫