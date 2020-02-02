import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

mycursor = conn.cursor()
sqlstr = 'UPDATE table01 SET tel = "6666666" WHERE tel = "02-1234567"'
mycursor.execute(sqlstr)

conn.commit()
conn.close()
