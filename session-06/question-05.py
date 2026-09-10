# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:31:21 2026

@author: AA
"""
students = {'Ali': [18, 17, 20],
            'Sara': [15, 19, 18],
            'Reza': [12, 14, 10],
            'Mina': [20, 20, 19]}

best_student = ''
highest_average = 0

for i in students:
    total = 0
    highest_score = 0

    for j in students[i]:
        total += j

        if j > highest_score:
            highest_score = j

    average = total / len(students[i])

    if average > highest_average:
        highest_average = average
        best_student = i

    if average >= 15:
        status = 'Passed'
    else:
        status = 'Failed'

    print(i, round(average, 2), status, highest_score)

print('Best student:', best_student)
print('Highest average:', round(highest_average, 2))