import requests
import datetime
import pandas as pd


def crawl_price(stock_id):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
    response = requests.post(url)
    
    with open('file.csv', 'w') as f:
        f.writelines(response.text)    
    df = pd.read_csv('file.csv', index_col = 'Date', parse_dates=['Data'])
    return df

df = crawl_price("2330.TW")
df.Close.plot()
#機器學習
#date = '2017'
#df.Close[date].plot()
#(df.Close.shift(-20) / df.Close > 1).astype(int)[date].plot(secondary_y=True)


date = '2019'
df.Close[date].plot()
(df.Close.shift(-100) / df.Close > 1).astype(int)[date].plot(secondary_y=True)

print(df)