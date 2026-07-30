# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:10:20 2026

@author: AA
"""

distance=float(input("Enter your traveled distance: "))
if distance <= 2:
    fare=20000
else:
        fare=(20000+((distance-2)*5000))
        
print("Total fare is: ",fare,"tomans")