# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
color1 = input("Enter color1: ")
color2 = input("Enter color2: ")
color3 = input("Enter color3: ")

if color1 == color2 == color3:
    print("All colors are the same.")
elif color1 == color2 or color1 == color3 or color2 == color3:
    print("Two colors are the same.")
else:
    print("Colors are not the same.")