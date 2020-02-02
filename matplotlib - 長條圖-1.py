import matplotlib.pyplot as plt
#class 對齊 
x = ['a', 'b', 'c', 'd', 'e']
#指定寬度
class_a = [90, 85, 45, 65, 80]
class_b = [60, 35, 75, 45, 90]
"""
plt.bar(x, class_a, label ='class_a')
plt.bar(x, class_b, label ='class_b')
"""
#label show class_a 在圖片上
plt.bar(x, class_a, label ='class_a', align = "center", width = 0.35)
#edge 分割
plt.bar(x, class_b, label ='class_b', align = "edge", width = 0.5)
"""
plt.bar(x, class_a, label ='class_a', align = "edge" , width = 0.35)
plt.bar(x, class_b, label ='class_b', align = "edge" , width = -0.35)
"""
# 如果要使用label要加這行
plt.legend() 
plt.title('sheet-name')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

