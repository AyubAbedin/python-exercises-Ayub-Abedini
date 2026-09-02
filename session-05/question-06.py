# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:44:52 2026

@author: AA
"""
j=0
list0=["hack", "fraud", "scam", "password", "attack"]

str0=input('Enter your sentence: ')
list1 = str0.split()

for i in list0:
    if i in list1:
        j = list1.count(i)
        print(i, "->", j)