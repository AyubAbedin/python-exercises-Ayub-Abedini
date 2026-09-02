# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:02:50 2026

@author: AA
"""
str0=''
str1=input('Enter a string: ')
for i in str1:
   if i not in str0:
      str0 = str0 + i
print (str0)