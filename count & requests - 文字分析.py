import requests
url = "https://health.udn.com/health/story/6008/4212145"
re = requests.get(url)
re.encoding = 'utf-8'
print(re.text)

ttext = re.text
sub = '喝水'
print ('喝水：',ttext.count(sub),'個字串')