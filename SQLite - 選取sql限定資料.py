import sqlite3
conn = sqlite3.connect('test.sqlite')

cursor = conn.execute('select * from table01 limit 3, -5')
#cursor = conn.execute('select * from table01 limit 3, -5')
#cursor = conn.execute('select * from table01 limit 3, 5')
#選擇 limit 3,5 指從第3筆資料開始找 -5是從倒數的開始算
rows = cursor.fetchall()

print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))

conn.close()