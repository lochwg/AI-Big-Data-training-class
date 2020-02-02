import matplotlib.pyplot as plt
x = ['a', 'b', 'c', 'd', 'e']
#給底線
class_a = [90, 85, 45, 65, 80]
class_a = [60, 35, 75, 45, 90]
#第幾列 第幾個欄位 第幾個


pie_color = ['yellow', 'plum', 'grey', 'brown', 'orange']
plt.pie(class_a, colors = pie_color, labels = x, autopct="%2.2f%%")

plt.title('123')
plt.xlabel('456')
plt.ylabel('789')