# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:05:11 2026

@author: AA
"""

products = {'P01': ('Laptop', 1200, 5),
            'P02': ('Phone', 800, 0),
            'P03': ('Tablet', 500, 12),
            'P04': ('Mouse', 50, 25),
            'P05': ('Keyboard', 100, 0) }

highest_value = 0
highest_product = ''


print('Available products:')

for i in products:
    product = products[i]

    if product[2] > 0:
        print(product[0])

print()

print('Out of stock products:')

for i in products:
    product = products[i]

    if product[2] == 0:
        print(product[0])

print()

print('The value of each product:')

for i in products:
    product = products[i]

    name = product[0]
    price = product[1]
    stock = product[2]

    value = price * stock

    print(name, ':', value)

    if value > highest_value:
        highest_value = value
        highest_product = name

print()

print('Product with highest value:')
print(highest_product, ':', highest_value)

print()

total_value = 0

for i in products:
    product = products[i]

    price = product[1]
    stock = product[2]

    value = price * stock

    total_value += value

print('Total STORE value:', total_value)