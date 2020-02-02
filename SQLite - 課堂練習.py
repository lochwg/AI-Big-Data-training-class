# =============================================================================
# 利用Python
# 1. 建立一個學生成績資料庫
# 2. 建立一個資料表
#     學號、姓名、國文、英文、數學
# 3. 新增6筆資料
# 4. 修改第三筆資料 國文為100
# 5. 刪除第四筆資料
# =============================================================================

# 1. 建立一個學生成績資料庫
import sqlite3
conn = sqlite3.connect('學員成績資料庫.sqlite')
cursor = conn.cursor()

# 2. 建立一個資料表 (學號、姓名、國文、英文、數學)
sqlstr = 'CREATE TABLE IF NOT EXISTS sem_01\
("學號" INTEGER PRIMARY KEY NOT NULL, "姓名" NOT NULL, "國文" NOT NULL, "英文" NOT NULL, "數學" NOT NULL)'
cursor.execute(sqlstr)

# 3. 新增6筆資料
_sqlstr = [(10801, 'LeBron James', '80', '70', '100'),
           (10802, 'Anthony Davis', '65', '80', '55'),
           (10803, 'Danny Green', '95', '40', '70'),
           (10804, 'Kyle Kuzma', '65', '80', '65'),
           (10805, 'Dwight Howard', '70', '55', '90'),
           (10806, 'JaVale MaGee', '60', '90', '100')]
cursor.executemany('insert into sem_01 values(?,?,?,?,?);', _sqlstr);
conn.commit()
conn.close() 

# 4. 修改第三筆資料 國文為100
update_sqlstr = 'UPDATE sem_01 SET 國文 = "100" WHERE 國文 = "95"'
cursor.execute(update_sqlstr)
conn.commit()
conn.close()

#5. 刪除第四筆資料
delete_sqlstr = 'delete from sem_01 WHERE 學號 = 10804'
cursor.execute(delete_sqlstr)
conn.commit()
conn.close() 
