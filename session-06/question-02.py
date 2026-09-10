# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:40:42 2026

@author: AA
"""
available = []
count_available = 0
stock = []
count_stock = 0
inventory = {'apple': 20,
             'banana': 5,
             'orange': 0,
             'milk': 12,
             'bread': 0}
for i in inventory:
    if inventory[i] != 0:
        available.append(i)
        count_available += 1
    else:
        stock.append(i)
        count_stock += 1       

print ('Available: ')
for i in available:
    print(i)

print ('Out of stock: ')
for i in stock:
    print(i)
    
print('Available count: ',count_available)
print('Out of stock count: ',count_stock)
