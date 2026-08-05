# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:55:55 2026

@author: AA
"""
# Customer Side
print('Salam be foroshghahe FNAVARI CO khosh omadid')
answer=input('aya mikhahid mahsooli ezafe konid? ')
answer = answer.strip()
answer = answer.lower()
if answer=='yes':
    print('bale ezafe mikonam')
elif answer=='no':
    print('mamnoon khedmat az mast')
else:
    print('shoma fagaht bayad ba yes/no javab bedi')