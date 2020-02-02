import pandas
df = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

df2 = df[0]
print (df2)
df3 = df2.iloc[0:2, 0:5] 
df3.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出']
print (df3)
df3.to_csv('data_df3.csv')

df4 = df3[u'幣別']
print(df4)
df5 = df3[u'幣別'].str.extract('\((\w+)\)')

print(df5)

df3[u'幣別'] = df3[u'幣別'].str.extract('\((\w+)\)')
#\w 表示[a_z, A_Z, 0_9]
#\w 非字母或數值

print(df3)
df3.to_excel('data_df3.xlsx')