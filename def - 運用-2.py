# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:14:00 2019

@author: TZE-YUAN
"""


#建立a b c 預設值為0
#避免空字串 或 無法呈現的數值 
#補值 例如將 c設定為預設值

def sum(a, b, c = 0):
    return a + b + c

print(sum(10, 20, 30)) 
print(sum(10, 20))