import re
import requests
from bs4 import BeautifulSoup
import os
import csv

folder_path = './photo/'
string = input('請輸入要尋找的字')
url = 'https://www.youtube.com/results?search_query=' + string

if (os.path.exists (folder_path) == False):
    os.makedirs(folder_path)

res = requests.get (url, verify = False)
soup = BeautifulSoup (res.text, 'html.parser')

last = None

with open ('youtube.csv', 'w', newline = '') as f:
    
    writer = csv.writer(f)
    writer.writerow ('ID')
    
    for entry in soup.select('a'):
        index = 0
        m = re.search('v=(.*)', entry['href'])
        if m:
            target = m.group(1)
            if target == last:
                continue
            if re.search('list', target):
                continue
            last = target
            print(target)
            writer.writerow([target])
            
            img_name = 'http://i.ytimg.com/vi/'+ target +'/0.jpg'
            jpg_name = folder_path + target + '.jpg' 

            print(img_name)
            html = requests.get(img_name)
            
            with open (jpg_name, 'wb') as file:
                
                file.write(html.content)
                file.flush()
            file.close()
            
f.close()