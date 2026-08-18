# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:59:13 2026

@author: AA
"""
c = 0
b = 0
s = [0, 0, 0, 0, 0, 0, 0, 0]
ss = [0, 0, 0, 0, 0, 0, 0, 0]
valid = True
p = input("رمز عبور را وارد کنید: ")
if len(p) != 8:
    print("    نامعتبر")
else:
    for i in range(8):
        if p[i].isdigit() == True:
            c = c + 1
            s[i] = 1
        elif p[i].isdigit() == False:
            b = b + 1
            ss[i] = 1
    if c == 4 and b == 4:
        for i in range(0, 4):
            if s[i] != 0 or ss[i] != 1:
                valid = False
        for i in range(4, 8):
            if s[i] != 1 or ss[i] != 0:
                valid = False
        if valid == True:
            print("    معتبر")
        else:
            print("    نامعتبر")
    else:
        print("    نامعتبر")
