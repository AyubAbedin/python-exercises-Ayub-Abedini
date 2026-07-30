# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:11:04 2026

@author: AA
"""

hour=int(input("Enter the hour (0-23): "))
if hour <0 or hour >23:
    print ("Invalid hour")
elif hour <= 5 or hour >= 20:
    print("Night")
elif hour>= 5 and hour <= 11:
    print("Morning")
elif hour>11 and hour <= 16:
    print("Afternoon")
elif hour > 16 and hour <=20:
    print("Evening")
