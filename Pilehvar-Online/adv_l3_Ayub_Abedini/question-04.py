# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:03:35 2026

@author: AA
"""
answer=input("ایا محصولی میخواهید؟ ")

while answer !="yes" and answer != "no":
    print("باید با yes و no جواب بدی")
    answer = input("ایا محصولی میخواهید؟ ")

if answer == "yes":
    print("بفرمایید")
elif answer == "no":
    print("بسیار عالی")