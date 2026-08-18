# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:59:13 2026

@author: AA
"""
import random
h=random.randint(1,10)
while True:
    num=int(input("Enter a number: "))
    if num > h:
      print ("Adad ra koochektar kon")
    elif num < h:
      print ("Adad ra bozorgtar kon")
    elif num == h:
      print ("**Tabrik shoma barnde shodin**")
      break