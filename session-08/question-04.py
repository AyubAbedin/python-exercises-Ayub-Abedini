# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:02:58 2026

@author: AA
"""

def get_values() -> list:
    """مقادیر را از کاربر دریافت می‌کند و در یک لیست قرار می‌دهد."""

    values = []
    number_of_values = int(input('Enter the number of values: '))

    for index in range(number_of_values):
        value = input('Enter a value: ')
        values.append(value)

    return values

#-------------------------------------------------------------------
def add_unique(value: str, unique_values: list) -> tuple:
    """مقدار را بررسی می‌کند و در صورت تکراری بودن موقعیت اولین ورود را برمی‌گرداند."""

    found_duplicate = False
    first_position = None

    for index in range(len(unique_values)):

        if unique_values[index].lower().strip() == value.lower().strip():
            found_duplicate = True
            first_position = index + 1
            break

    if found_duplicate == False:
        unique_values.append(value)

    return first_position, unique_values

#-------------------------------------------------------------------
def process_values(values: list) -> tuple:
    """مقادیر را بررسی می‌کند و اطلاعات یکتا و تکراری را آماده می‌کند."""

    duplicate_count = 0
    unique_values = []
    first_positions = []

    for index in range(len(values)):
        value = values[index]

        first_position, unique_values = add_unique(value, unique_values)

        if first_position != None:
            duplicate_count += 1

    for unique_value in unique_values:
        for index in range(len(values)):
            if unique_value.lower().strip() == values[index].lower().strip():
                first_positions.append(index + 1)
                break

    unique_count = len(unique_values)

    return duplicate_count, unique_count, unique_values, first_positions

#-------------------------------------------------------------------
def show_report(unique_values: list, duplicate_count: int,
                unique_count: int, first_positions: list) -> None:
    """گزارش نهایی مقادیر یکتا، تکراری و موقعیت اولین ورود را نمایش می‌دهد."""

    print()
    print('Unique values:', unique_values)
    print('Duplicate values count:', duplicate_count)
    print('Unique values count:', unique_count)
    print()
    print('First positions:')

    for index in range(len(unique_values)):
        print(unique_values[index], '-->', first_positions[index])

#-------------------------------------------------------------------
# Function calls
values = get_values()
duplicate_count, unique_count, unique_values, first_positions = process_values(values)
show_report(unique_values, duplicate_count, unique_count, first_positions)





