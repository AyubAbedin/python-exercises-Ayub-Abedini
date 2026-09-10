# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:44:41 2026

@author: AA
"""

products = {'laptop': 1200,
            'phone': 800,
            'tablet': 500,
            'headphone': 150,
            'mouse': 50}
max_value = max(products.values())
min_value =min(products.values())
a = ''
c = ''
f = []
sum0 = 0

t = len(products)

for i in products:
    
   if products[i] == max_value:
      a = i
      
   if products[i] == min_value:
      c = i

   if products[i]>500:
      f.append(i)
      
   sum0 += products[i]
   
average_price = sum0/t
    
print('Most Expensive Products: ', a)
print('Cheapest Products: ',c)
print('Average Price of Products: ', average_price)
print('Products with Price over 500: ', end='')
for i in f:
    print(i,end=', ')
print()
print('Total Price of Products: ', sum0)
