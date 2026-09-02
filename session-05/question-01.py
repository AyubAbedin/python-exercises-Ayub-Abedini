# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:35:12 2026

@author: AA
"""
upercae=0
lowercase=0
number=0
character=0

passw=input("Enter Password: ")
if len(passw) < 8:
    print('Paeeword is invalid')
    print("Password must contain at least 8 characters")
else:
    for pas in passw:
      if pas.isupper():
         upercae += 1
      elif pas.islower():
         lowercase += 1
      elif pas.isdigit():
         number += 1
      elif not pas.isalnum():
         character += 1
    if upercae >= 1 and lowercase >= 1 and number >= 1 and character >= 1:
       print('Password is valid')
    
    if upercae == 0:
      print('Pasword is invali')
      print('Password must contain a Uppercase character')

    if lowercase == 0:
      print('Pasword is invali')
      print('Password must contain a Lowercase character')

    if number == 0:
      print('Pasword is invali')
      print('Password must contain a Number')

    if character == 0:
      print('Pasword is invali')
      print('Password must contain a spacial character ! @ # $')