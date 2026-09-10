# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:00:22 2026

@author: AA
"""

sales = ( ('Ali', 'Laptop', 1200),
          ('Sara', 'Phone', 800),
          ('Ali', 'Phone', 800),
          ('Reza', 'Laptop', 1200),
          ('Sara', 'Laptop', 1200),
          ('Ali', 'Mouse', 50) )

customers = {}
products = {}
highest_purchase = 0
best_customer = ''
total_sales = 0

for i in sales:
    total_sales += i[2]
    j = i[0]
    k = i[1]
    price = i[2]

    if j in customers:
        customers[j] += price
    else:
        customers[j] = price
        
    if k in products:
        products[k] += 1
    else:
        products[k] = 1

print('Customer purchases:')

for i in customers:
    print(i, '-->', customers[i])
    
for i in customers:
    if customers[i] > highest_purchase:
        highest_purchase = customers[i]
        best_customer = i
print()

print('Customer with highest purchase:')
print(best_customer, ':', highest_purchase)

print()

print('Product sales count:')
for i in products:
    print(i, ':', products[i])
    
print()

print('Total store revenue:', total_sales)