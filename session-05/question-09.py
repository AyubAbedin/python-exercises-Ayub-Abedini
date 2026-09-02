# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:50:52 2026

@author: AA
"""
username="Ayub Abedini"
password="123456789"
for i in range(1,4):
    user_name=input("Enter your username: ")
    passw=input("Enter your password: ")
    if user_name==username and passw==password:
        print("Login successful")
        break
    else:
         print("Wrong username or password")
         print("Atempts remaining: ",3-i)
