import pandas as pd
tables = pd.read_html("http://ppg.naif.org.tw/naif/MarketInformation/Reference/reference.aspx"\
                      ,encoding="utf-8")

#步驟一、尋找需要的表格內容
# =============================================================================
# n = 1
# for table in tables:
#     print("第" + str(n) + "個表格：")
#     print(table.head())
#     print()
#     n += 1
# =============================================================================
#步驟二、找到第3的表格
table = tables[2]
table.columns = ["年度","","12月","11月","10月","9月","8月"\
                 ,"7月","6月","5月","4月","3月","2月","1月"]
table.index = range(len(table.index))
print(table)
df.astype(float)
df.plot()


