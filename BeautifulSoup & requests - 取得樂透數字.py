import bs4, requests

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)
print ('網頁下載中 ...')
html.raise_for_status()
print ('網頁下載完成')

objSoup = bs4.BeautifulSoup(html.text, 'lxml')

dataTag = objSoup.select('.contents_box02')
print('串列長度', len(dataTag))
for i in range(len(dataTag)):
    print(dataTag[i])
    
balls = dataTag[0].find_all('div', {'class':'ball_tx ball_green'})
print('開出順序:', end='')
for i in range(6):
    print(balls[i].text, end='')

print('\n大小順序:', end='')
for i in range(6, len(balls)):
    print(balls[i].text, end='')
    
redball = dataTag[0].find_all('div', {'class':'ball_red'})
print('\n第二選區:', redball[0].text)
