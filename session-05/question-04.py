# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:03:35 2026

@author: AA
"""
max_cont=0
str0=''
str1=input('Enter a your sentense: ')
list0=str1.split()
for i in list0:
   if max_cont < list0.count(i):
      max_cont=list0.count(i)
      str0=i
print(str0,'->',max_cont)
