import requests
from collections import Counter
url = "https://health.udn.com/health/story/6008/4212145"
re = requests.get(url)
re.encoding = 'utf-8'
ttext = re.text
print (ttext)

b = dict(Counter(ttext))
print(b)

print([key for key, value in b.items() if value > 20])