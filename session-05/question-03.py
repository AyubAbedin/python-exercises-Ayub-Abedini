# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:03:20 2026

@author: AA
"""
e=0
b=0
k=0
n=0
s=0
kh=0
str0=input('Enter a strin:')
for i in str0:
   if 'A'<=i<='Z':
      e+=1
      b+=1
   elif 'a'<=i<='z':
      k+=1
      e+=1
   elif i.isdigit():
      n+=1
   elif i==' ':
      s+=1
   else:
       kh+=1
print('Letters: ',e)
print('Uppercase: ',b)
print('Lowercase: ',k)
print('Digits: ',n)
print('Spaces: ',s)
print('Special charcters: ',kh)
