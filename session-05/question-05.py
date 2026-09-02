# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:41:07 2026

@author: AA
"""

max_len = 0
str0 = ''

str1 = input('Enter your sentence: ')
list0 = str1.split()

for i in list0:
    if len(i) > max_len:
        max_len = len(i)
        str0 = i

print("Longest word:", str0)
print("Length:", max_len)