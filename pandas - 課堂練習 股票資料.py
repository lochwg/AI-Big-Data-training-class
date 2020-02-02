
import pandas
df = pandas.read_html('http://jsjustweb.jihsun.com.tw/z/zc/zcv/zcvz/zcvz_60C841B8-F5D5-436F-A47C-924B4F5B8BAE.djhtm')

df2 = df[0]
print (df2)
df3 = df2.iloc[4:46, 0:7] 
df3.columns = [u'簡稱', u'代號', u'標的', u'最後交易日', u'終止上市日', u'履約價', u'行使比例']
print (df3)
df3.to_csv('data_stock.csv')
