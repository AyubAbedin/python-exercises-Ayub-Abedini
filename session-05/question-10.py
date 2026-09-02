# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:50:16 2026

@author: AA
"""
sentence1=input("Enter sentence 1: ")
sentence2=input("Enter sentence 2: ")
list1 = sentence1.split()
list2 = sentence2.split()

for i in list1:
    if i in list2:
        print("Common words:",i)