# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:59:13 2026

@author: AA
"""
sum1=0
while True:
     num=int(input("Enter a number (0 to stop): "))
     if num!=0:
       sum1=sum1+num
     else:
       print("The Sum is: ",sum1)
       break
