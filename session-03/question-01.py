# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""

numbers=[15,50,70,1,90,20,4,108,6]
max_number=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
print("Max number is:", max_number)