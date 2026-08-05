# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:07:53 2026

@author: AA
"""
# Customer Side
products=["laptop", "mouse", "keyboard", "monitor", "printer"]
print('Salam be foroshghahe FNAVARI CO khosh omadid')
answer=input('aya mikhahid mahsooli ezafe konid? ')
answer = answer.strip()
answer = answer.lower()
if answer=='yes':
    print('bale ezafe mikonam')
    product=input('name mahsool ra vared konid: ')
    products.append(product)
    print (products)
elif answer=='no':
    print('mamnoon khedmat az mast')
else:
    print('shoma fagaht bayad ba yes/no javab bedi')