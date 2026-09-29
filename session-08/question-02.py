# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:25:10 2026

@author: AA
"""

file_path = 'C:/Users/AA/Documents/GitHub/python-exercises-Ayub-Abedini/session-08/logs.txt'

#-------------------------------------------------------------

def count_successful_logins() -> int:
    """لاگین‌های موفق را محاسبه می‌کند."""

    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[1] == 'LOGIN' and parts[2] == '200':
                count += 1

    return count

#-------------------------------------------------------------

def count_failed_logins() -> int:
    """لاگین‌های ناموفق را محاسبه می‌کند."""

    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[1] == 'LOGIN' and parts[2] == '403':
                count += 1

    return count

#-------------------------------------------------------------

def find_suspicious_users() -> list:
    """کاربران دارای حداقل 3 خطای 403 را پیدا می‌کند."""

    suspicious_users = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[1] == 'LOGIN' and parts[2] == '403':

                if parts[0] in suspicious_users:
                    suspicious_users[parts[0]] += 1
                else:
                    suspicious_users[parts[0]] = 1

    suspicious = []

    for key, value in suspicious_users.items():

        if value >= 3:
            suspicious.append(key)

    return suspicious

#-------------------------------------------------------------

def generate_report() -> None:
    """گزارش کاملی از لاگ‌ها را نمایش می‌دهد."""

    successful = count_successful_logins()
    failed = count_failed_logins()
    suspicious = find_suspicious_users()

    operations = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[0] in operations:
                operations[parts[0]] += 1
            else:
                operations[parts[0]] = 1

    print('----------------------------------------')
    print('              LOG REPORT')
    print('----------------------------------------')
    print()
    print('[1] LOGIN RESULTS')
    print('Successful logins :', successful)
    print('Failed logins     :', failed)
    print()
    print('[2] SUSPICIOUS USERS')

    if len(suspicious) == 0:
        print('No suspicious users found.')
    else:
        for user in suspicious:
            print('-', user)

    print()
    print('[3] OPERATIONS PER USER')

    for key, value in operations.items():
        print(f'- {key}: {value} operations')

    print()
    print('----------------------------------------')

#-------------------------------------------------------------
# Function calls

generate_report()