import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS table01 \
("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'

#\為分行符號，教學用 亦可表示為
#sqlstr = 'CREATE TABLE IF NOT EXISTS table01("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'
cursor.execute(sqlstr)

sqlstr = 'insert into table01 values(1, "02-1234567")'
cursor.execute(sqlstr)

conn.commit()
conn.close() 


