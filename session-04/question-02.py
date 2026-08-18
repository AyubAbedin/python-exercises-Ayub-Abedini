# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:59:13 2026

@author: AA
"""
import random
while True:
    user=input("Enter sang, kaghaz, or gaychi: ")
    computer=random.choice(["sang","kaghaz","gaychi"])
    print("Entekhabe computer: ",computer)
    if user=="Exit" or user=="exit":
        print("Game Over!")
        break
    elif user not in ["sang" , "kaghaz" , "gaychi"]:
        print("Warning: Please enter sang, kaghaz, or gaychi!")
        continue
    elif (user=="sang" and computer=="gaychi") or\
         (user=="kaghaz" and computer=="sang") or \
         (user=="gaychi" and computer=="kaghaz"):
        print("**You are Win!**")
    elif (computer=="sang" and user=="gaychi") or\
         (computer=="kaghaz" and user=="sang") or \
         (computer=="gaychi" and user=="kaghaz"):
        print("**Computer is Win!**")
    elif user==computer:
       print ("Mosavi! Dobare talash konid.")
