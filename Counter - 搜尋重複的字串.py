from collections import Counter
a = [29, 36, 57, 12, 79, 43, 23, 56, 28,\
     11, 14, 15, 16, 37, 24, 35, 17, 24]
b = dict(Counter(a))
print ([Key for Key, value in b.items()if value >1])
print (b)