import requests
import time

for i in range(1, 3): #執行次數 2次
    ress = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=&selectType=&_=1574671625496')
    time.sleep(5)
    print(ress)