import pandas as pd
tables = pd.read_html("http://www.stockq.org/market/commodity.php")
table = tables[7]

#測試一、顯示商品、買價、漲跌、比例、台北
table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))
print(table)

#測試二、顯示商品、買價
table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))
print(table.loc[:,"商品":"買價"])

# =============================================================================
# import matplotlib.pyplot as plt
# plt.hist(table["買價"])
# plt.show()
# =============================================================================

