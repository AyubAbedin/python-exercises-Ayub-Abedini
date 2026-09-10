# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:00:36 2026

@author: AA
"""
dic = {}
special_char = [' ', '!', '@', '#', '$', '%', '&']

str0 = input('Enter a String: ')

for i in str0:
    if i not in special_char:
       if i in dic:
         dic[i] = dic[i] + 1
       else:
         dic[i] = 1
print(dic)