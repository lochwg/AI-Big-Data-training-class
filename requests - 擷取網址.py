import requests

url = 'https://www.pexels.com/zh-tw/'
try:
    htmlfile = requests.get(url)
    print('下載成功')
except Exception as err:
    print('網頁下載失敗: %s' % err)
    
fn = 'out_414.txt'
with open(fn, 'wb') as file_Obj:
    for diskstorage in htmlfile.iter_content(10240):
        size = file_Obj.write(diskstorage)
        print(size)
    print('以 %s 儲存網頁HTML檔案成功' % fn)