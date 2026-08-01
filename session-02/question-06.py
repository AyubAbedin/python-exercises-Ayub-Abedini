# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:10:34 2026

@author: AA
"""
price = float(input("Enter purchase amount: "))
if price > 1000000:
    discount = 15
    final_price = (price-(price*0.15))
elif 500000 <= price <= 1000000:
    discount = 10
    final_price = (price-(price*0.1))
elif price < 500000:
     final_price = price
     discount=0
print("Final Price is: ",final_price,"Discount is: ", discount,"%")

    
    
