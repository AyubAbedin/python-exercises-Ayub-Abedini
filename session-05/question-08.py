# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:51:21 2026

@author: AA
"""

let=0
u=0
l=0
n=0
s=0
shortest=" "
longest=" "
most_word = ''
max_word = 0
most_char = ''
max_char = 0
str0=input('Enter a your text: ')
list0=str0.split()
t_char=len(str0)
t_word=len(list0)
for i in str0:
    if "A" <= i <= "Z":
        let += 1
        u += 1
    elif "a" <= i <= "z":
        let += 1
        l += 1
    elif i.isdigit():
        n += 1
    elif i == ' ':
        s += 1

longest=list0[0]
shortest=list0[0]
for i in list0:
    if len(i)>len(longest):
        longest=i
    if len(i)<len(shortest):
        shortest=i

for i in str0:
    if str0.count(i) > max_char:
        max_char = str0.count(i)
        most_char = i

for i in list0:
    if list0.count(i) > max_word:
        max_word = list0.count(i)
        most_word = i

print("Total characters: ",t_char)
print("Total words: ",t_word)
print("Total letters: ",let)
print("Total digite: ",n)
print("Total uppercases: ",u)
print("Total lowercases: ",l)
print("Longes word: ",longest)
print("Shortest word: ",shortest)
print("Most repeated character: ",most_char)
print("Most repeated word: ",most_word)