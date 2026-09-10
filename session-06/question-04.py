# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:34:17 2026

@author: AA
"""
max_salary = 0
min_salary = 100000
max_name = ''
min_name = ''
high_salary = []
sum_salary = 0

employees = {'E01': {'name': 'Ali', 'age': 28, 'salary': 3000},
             'E02': {'name': 'Sara', 'age': 32, 'salary': 4500},
             'E03': {'name': 'Reza', 'age': 25, 'salary': 2800} }

for i in employees:
    for j in employees[i]:

        if j == 'salary':

            if employees[i][j] > max_salary:
                max_salary = employees[i][j]
                max_name = employees[i]['name']

            if employees[i][j] < min_salary:
                min_salary = employees[i][j]
                min_name = employees[i]['name']

            if employees[i][j] > 3000:
                high_salary.append(employees[i]['name'])

            sum_salary += employees[i][j]

average_salary = sum_salary / len(employees)

print('Highest salary:', max_name, max_salary)
print('Average salary:', round(average_salary,2))
print('Salary over 3000:', end='')
for i in high_salary:
    print(i)
print('Lowest salary:', min_name)