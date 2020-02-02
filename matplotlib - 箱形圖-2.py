
# =============================================================================
# 取代指令
# pp1 = pp.replace ("-", 0)
# pp1.to_excel('excel_output.xls')
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
csv_data = pd.read_csv(r"", engine = 'python')

pp = csv_data[['C1', 'D1']].head(10)
pp1 = pp.replace ('-', 0)
print(pp1)
pp1.to_excel('excel_output.xls')

plt.plot(pp1)
plt.title('AAAA')
plt.show()