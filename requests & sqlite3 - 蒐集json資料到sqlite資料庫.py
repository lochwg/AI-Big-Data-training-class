import sqlite3, ast, hashlib, os, requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('DataPM25_2019.sqlite')
cursor = conn.cursor()

sqlstr ='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT
NOT NULL UNIQUE , "SiteName" TEXT NOT NULL , "PM25" INTERGER)
''' 
cursor.execute(sqlstr)
url = "http://opendata2.epa.gov.tw/AQI.json"

html = requests.get(url).text.encode('utf-8-sig')

md5 = hashlib.md5(html).hexdigest()
old_md = ""

if os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r') as f:
        old_md5 = f.read()
    with open('old_md5.txt', 'w') as f:
        f.write(md5)
        
if md5 != old_md5:
    print('資料已更新 ...')
    sp = BeautifulSoup(html, 'html.paser')
    
    jsondata = ast.literal_eval(sp.text)
    
    conn.execute("delete from TablePM25")
    conn.commit()
    
    n=1
    for site in jsondata:
        SiteName = site["SiteName"]
        if site["PM2.5"] == "ND":
            continue
        PM25 = 0 if site["PM2.5"] == "" else int(site["PM2.5"])
        print("站名:{} PM2.5={}".format(SiteName, PM25))

        sqlstr = "insert into TablePM25 values({}, '{}', {})".format(n, SiteName, PM25)
        cursor.execute(sqlstr)
        n += 1
        conn.commit()
        
else:
    print('資料未更新，從資料庫讀取 ...')
    cursor = conn.execute("select * from TablePM25")
    rows = cursor.fetchall()
    for row in rows:
        print("站名:{} PM2.5={}".format(row[1],row[2]))
    
    