import requests
import json
import csv

ress = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=&selectType=&_=1574671625496')
print (ress.text)
print ('----------(json)以下將data部分轉出----------')

jsontxt = json.loads(ress.text)

for data in (jsontxt['data']):
    print(data)
print ('----------以下存成檔案----------')
outputfile = open(r'_test_stock.csv', 'w', newline='')
outputwriter = csv.writer(outputfile)
outputwriter.writerow(jsontxt['title'])
outputwriter.writerow(jsontxt['fields'])
for data in (jsontxt['data']):
        outputwriter.writerow(data)
outputwriter.close()    