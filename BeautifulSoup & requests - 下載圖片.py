import bs4, requests, os

url = 'https://pixabay.com/zh/images/search/'
html = requests.get(url)
print('網頁下載中 ...')
html.raise_for_status()
print('網頁下載完成')

destDir = 'Photo_01'
if os.path.exists(destDir) == False:         #如果目錄不存在
    os.mkdir(destDir)                        #用數字權限模式建立目錄
    
objSoup = bs4.BeautifulSoup(html.text, 'lxml')      

imgTag = objSoup.select('img')                  #搜尋出所有圖片檔案
print ('搜尋到的圖數量 = ', len(imgTag))         #列出搜尋到的圖片數
if len(imgTag) > 0 :                            #如果有找到圖片則
    for i in range(len(imgTag)):                #迴圈下載圖片與儲存
        imgUrl = imgTag[i].get('src')           #取得圖片的路徑
        print('%s 圖片下載中 ... ' % imgUrl)
        if ('http' not in imgUrl):
            if ('svg' in imgUrl):
                url = 'https://pixabay.com'
                finUrl = url + imgUrl
            else:
                imgUrl = imgTag[i].get('data-lazy')
            #finUrl = url + imgUrl
                finUrl = imgUrl
                
        else:
            finUrl = imgUrl
        #finUrl = url + imgUrl 相對路徑   #取得圖片在Internet上的
        #絕對路徑
        print('%s 圖片下載中 ... ' % finUrl)
        picture = requests.get(finUrl)          #下載圖片
        picture.raise_for_status()              #驗證圖片是否下載成功
        print('%s 圖片下載中 ... ' % finUrl)
        
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()
        
        