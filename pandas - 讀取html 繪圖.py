import pandas as pd
tables = pd.read_html("http://www.stockq.org/market/commodity.php")
table = tables[7]

table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))
print(table.loc[:,"商品":"買價"])


_table = table.loc["黃金":"鉛","商品":"買價"]
_table = _table.astype(float)
_table.plot()
