# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
text=input("Enter a text: ")

str_length=len(text)

if str_length%2==0:
    print(text[:str_length//2])
else:
    print(text[str_length//2:])
