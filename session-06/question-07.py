# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:23:39 2026

@author: AA
"""

orders = [ ('Ali', 'Laptop'),
          ('Sara', 'Phone'),
          ('Ali', 'Phone'),
          ('Reza', 'Laptop'),
          ('Sara', 'Laptop'),
          ('Ali', 'Tablet'),
          ('Reza', 'Phone') ]

customers = {}

for i in orders:
    if i[0] in customers:
        customers[i[0]].append(i[1])
    else:
        customers[i[0]] = [i[1]]

print(customers)