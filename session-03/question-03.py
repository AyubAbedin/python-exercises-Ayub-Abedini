# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
sum_numbers=0
for i in range(1, 11):
    if i%2==1:
        result=i*5
    elif i%2==0:
        result=i+5
    sum_numbers=sum_numbers+result
print("Sum= ", sum_numbers)