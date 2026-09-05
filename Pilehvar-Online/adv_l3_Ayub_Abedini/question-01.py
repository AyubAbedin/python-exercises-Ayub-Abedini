"""
Created on Tue Sep  1 22:35:12 2026

@author: AA
"""
passw=input("Enter your password: ")
num=0
let=0
upper=0
lower=0
for i in passw:
    if i.isdigit():
        num+=1
    if i.isalpha():
        let+= 1
    if i.isupper():
        upper+= 1
    if i.islower():
        lower+= 1

if len(passw) > 8 and num >= 1 and let >= 1 and upper >= 1 and lower >= 1:
    print("با موفقیت ثبت شد.")