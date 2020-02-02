import pandas
df = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

df2 = df[0]
#print(len(df))
print (df2)
#type(df2)
#pandas.core.frame.DataFrame

df3 = df2.iloc[0:2, 0:5] #左邊是index 右邊是column 0:2有 2筆資料 要-1
df3.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出']
print (df3)
df3.to_csv('data_df3.csv')