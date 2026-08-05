# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
number1=float(input("Enter number1: "))
number2=float(input("Enter number2: "))
operator=input("Enter operator (+,-,*,/): ")
if operator=="+":
    print('number1+number2= ',number1+number2)
elif operator=="-":
    print('number1-number2= ',number1-number2)
elif operator=="*":
    print('number1*number2= ',number1*number2)
elif operator=="/":
    print('number1/number2= ',number1/number2)
else:
    print("Invalid operator")
