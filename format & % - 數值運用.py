"""
程式的規則 '由左至右' '由上到下'
註解 crtl + 1
多行註解 crtl + 4
"""
#指定寬度
msg = '(%10s)' % 'Hello'
print(msg)
msg1 = '%s' % 'Hello'
print(msg1)

#靠左對齊
msg2 = '(%-10s)' % 'hello'
print(msg2)

#自動四捨五入 8.3指 8位數.3位數 f浮點數
msg3 = '(%8.3f)' % 12.3456
print(msg3)

#文字長度上限 s 字串
msg4 = '(%.3s)' % 'hello'
print(msg4)

"""
%10s 代表靠右 %-10s 代表靠左
%1s 不代表限制 是寬度 %1s => hello 
%.3s 代表限制 
% 轉換/ %s字串 %d 數值
"""

"""
format的格式 無法用 - 代表靠左對齊
"""

#指定寬度 :10 10個位元 字數的寬度
msg5 = '({:10})'.format('abcdefghijklm')
print(msg5)

#靠左對齊
msg6 = '({:<10})'.format('hello')
print(msg6)
#靠右對齊
msg7 = '({:>10})'.format('hello')
print(msg7)
#置中對齊
msg8 = '({:^10})'.format('hello')
print(msg8)


# % 轉換符號*()
# {} 轉換符號 .format

#小數點也算一位
msg9 = '%08.2f' % 3.14159
print(msg9)
#加上正負號
msg10 = '%+4.2f, %+4.2f' % (3.14, -3.14)
print(msg10)

#負數加負號，正數留空白
msg11 = ' (% d), (% d)' % (3, -3)
print(msg11)

#空白補0 
msg12 = '{:08.2f}'.format(3.14159)
print(msg12)

#加上正負號
msg13 = '{:+4.2f}, {:+4.2f}'.format(3.14, -3.14)
print(msg13)

#負數加負號，正數留空白
msg14 = '({: d}), ({: d})'.format(3, -3)
print(msg14)












