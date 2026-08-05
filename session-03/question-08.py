# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:52:05 2026

@author: AA
"""
mojoodi = float(input("Mojoodi hesab ra vared konid: "))
bardasht = float(input("Mablagh bardasht ra vared konid: "))

if bardasht <= 0:
    print("Mablagh bardasht na motabar ast")

elif bardasht > mojoodi:
    print("Mojoodi kafi nist")

else:
    mojoodi = mojoodi - bardasht
    print("Bardasht movafagh anjam shod")
    print("Mojoodi baghimande:", mojoodi)