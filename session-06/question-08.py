# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:28:53 2026

@author: AA
"""

users = [ ('Ali', 25, 'Python'),
          ('Sara', 30, 'Java'),
          ('Reza', 22, 'Python'),
          ('Mina', 28, 'C++'),
          ('John', 35, 'Python'),
          ('David', 30, 'Java') ]

languages = {}
ages = {}
oldest_age = {}
oldest_name = {}
most_users = 0
best_language = ''

for i in users:

    name = i[0]
    age = i[1]
    lang = i[2]

    if lang in languages:
        languages[lang].append(name)
    else:
        languages[lang] = [name]

    if lang in ages:
        ages[lang].append(age)
    else:
        ages[lang] = [age]

    if lang not in oldest_age:
        oldest_age[lang] = age
        oldest_name[lang] = name

    elif age > oldest_age[lang]:
        oldest_age[lang] = age
        oldest_name[lang] = name


print('Users by language:')
for i in languages:
    print(i, ':', languages[i])

print()

print('Average age:')
for i in ages:
    total = 0

    for j in ages[i]:
        total += j

    average = total / len(ages[i])

    print(i, ':', round(average, 2))

print()

print('Oldest user of each language:')
for i in oldest_name:
    print(i, ':', oldest_name[i], '-', oldest_age[i])
    
for i in languages:
    count = len(languages[i])

    if count > most_users:
        most_users = count
        best_language = i

print('Language with most users:', best_language)
print('Number of users:', most_users)

for i in languages:
    print(i)