# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:51:44 2026

@author: AA
"""
j=1
str0=input('Enter a your text: ')
for i in range(len(str0)-1):
   if str0[i] == str0[i+1]:
      j+=1
   else:
       print(str0[i],j,sep='',end="")
       j=1
print(str0[i],j,sep='',end='')
