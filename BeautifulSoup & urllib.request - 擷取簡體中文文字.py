import urllib.request
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def getWord(html):
    bs = BeautifulSoup(html, 'html.parser')
    namelist = bs.findAll('a')
    return namelist

url = "http://toutiao.sogou.com/guonei.html"
html = getHtml(url)
namelist = getWord(html)

for name in namelist:
    print(name.get_text())