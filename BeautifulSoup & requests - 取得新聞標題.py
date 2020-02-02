import bs4, requests

url = 'https://www.chinatimes.com/?chdtv'
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()   #驗證網頁是否下載成功
print("網頁下產完成")

objSoup = bs4.BeautifulSoup(html.text, 'lxml')  

dataTag = objSoup.select('.top')  # 尋找class是contents_box02
print('串列長度', len(dataTag))
for i in range(len(dataTag)):
    print(dataTag[i])               
    #(dataTag[i].find_all('h4', {'class':'title'}).text)
Title = dataTag[0].find_all('h4', {'class':'title'})
print('\n標題：', Title[0].text)