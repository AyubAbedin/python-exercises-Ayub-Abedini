# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:14:10 2026

@author: AA
"""

file_path = 'C:/Users/AA/Documents/GitHub/python-exercises-Ayub-Abedini/session-08/users.txt'

#---------------------------------------------------------------------

def add_user(username: str, password: str, status: str) -> None:
    """یک کاربر جدید را به فایل اضافه می‌کند."""

    found = False

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[0] == username:
                found = True
                break

    if found:
        print(f'Already exists: {username}')
    else:
        with open(file_path, 'a') as file:
            file.write(f'{username},{password},{status}\n')

        print(f'Added: {username},{password},{status}')

#---------------------------------------------------------------------

def find_user(username: str) -> None:
    """کاربر موردنظر را پیدا کرده و اطلاعات آن را نمایش می‌دهد."""

    found = False

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[0] == username:
                print(f'Found: {parts[0]},{parts[1]},{parts[2]}')

                found = True
                break

    if not found:
        print(f'User not found: {username}')

#---------------------------------------------------------------------

def delete_user(username: str) -> None:
    """کاربر موردنظر را از فایل حذف می‌کند."""

    users = []
    found = False

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[0] == username:
                found = True
            else:
                users.append(line)

    if found:
        with open(file_path, 'w') as file:
            for user in users:
                file.write(user)

        print(f'Deleted: {username}')
    else:
        print(f'User not found: {username}')

#---------------------------------------------------------------------

def generate_report() -> None:
    """تعداد کاربران فعال و مسدود را نمایش می‌دهد."""

    active_users = 0
    blocked_users = 0

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[2] == 'active':
                active_users += 1

            elif parts[2] == 'blocked':
                blocked_users += 1

    print('Active  :', active_users)
    print('Blocked :', blocked_users)

#---------------------------------------------------------------------
# Function calls

print('----------------------------------------')
print('            USER MANAGEMENT')
print('----------------------------------------')
print()
print('[1] ADD USERS')
add_user('Mohammad', '12345', 'active')
add_user('Nima', '67890', 'blocked')
add_user('Sara', '99999', 'active')
print()
print('[2] FIND USERS')
find_user('Ali')
find_user('Mohammad')
find_user('Hossein')
print()
print('[3] DELETE USERS')
delete_user('Reza')
delete_user('Hossein')
print()
print('[4] USER REPORT')
generate_report()
print('----------------------------------------')