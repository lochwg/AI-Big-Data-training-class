import pandas as pd

url = 'http://www.stockq.org/market/asia.php'
table = pd.read_html(url)[4]
table = table.drop(table.columns[[1, 2]], axis = 0)
table = table.drop(table.columns[9:15], axis = 1)