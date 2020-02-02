import sqlite3
conn = sqlite3.connect('test.sqlite')
mycursor = conn.cursor()

sqlstr = 'delete from table01 WHERE num = 3'

mycursor.execute(sqlstr)

conn.commit()
conn.close()