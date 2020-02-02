from bs4 import BeautifulSoup
from urllib.request import urllib.request
import jieba
from collections import Counter

def getHtml(url):
    page = urlopen(url)
    html = page.read().decode('utf-8-sig')
    return html

def getWord(html):
    sp = BeautifulSoup(html, 'html.parser')
    data = sp.find_all('h3')
    return data

url = 'https://www.most.gov.tw/folksonomy/list?menu_ic'
html = getHtml(url)
words = getWord(html)

list1 = []
for word in words:
    w = jieba.cut(word.text.strip(), cut_all=False)
    
    for item in w:
        if item != None and 
    
    
    


