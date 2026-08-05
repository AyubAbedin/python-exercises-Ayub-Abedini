# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
max_jump=0
for i in range(0,10):
    jump=float(input("Enter jump height: "))
    if jump > max_jump:
        max_jump=jump
        print("New Record")
    else:
        print("Record was not Broken.")
print("Highest jump:", max_jump)