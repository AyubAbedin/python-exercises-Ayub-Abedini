# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:25:48 2026

@author: AA
"""
file_path = 'C:/Users/AA/Documents/GitHub/python-exercises-Ayub-Abedini/session-08/transactions.txt'

#-----------------------------------------------------------------------

def calculate_balance() -> dict:
    """موجودی نهایی هر کاربر را محاسبه می‌کند."""

    balance = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            name = parts[0]
            transaction_type = parts[1]
            amount = int(parts[2])

            if name not in balance:
                balance[name] = 0

            if transaction_type == 'deposit':
                balance[name] += amount

            elif transaction_type == 'withdraw':
                if amount <= balance[name]:
                    balance[name] -= amount

    return balance

#-----------------------------------------------------------------------

def total_deposits() -> dict:
    """مجموع واریزهای هر کاربر را محاسبه می‌کند."""

    deposits = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            name = parts[0]
            transaction_type = parts[1]
            amount = int(parts[2])

            if transaction_type == 'deposit':
                if name in deposits:
                    deposits[name] += amount
                else:
                    deposits[name] = amount

    return deposits

#-----------------------------------------------------------------------

def total_withdrawals() -> dict:
    """مجموع برداشت‌های هر کاربر را محاسبه می‌کند."""

    withdrawals = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            name = parts[0]
            transaction_type = parts[1]
            amount = int(parts[2])

            if transaction_type == 'withdraw':
                if name in withdrawals:
                    withdrawals[name] += amount
                else:
                    withdrawals[name] = amount

    return withdrawals

#-----------------------------------------------------------------------

def find_invalid_transactions() -> list:
    """تراکنش‌های برداشت بیشتر از موجودی را پیدا می‌کند."""

    balance = {}
    invalid_transactions = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            name = parts[0]
            transaction_type = parts[1]
            amount = int(parts[2])

            if name not in balance:
                balance[name] = 0

            if transaction_type == 'deposit':
                balance[name] += amount

            elif transaction_type == 'withdraw':
                if amount > balance[name]:
                    invalid_transactions.append(line.strip())
                else:
                    balance[name] -= amount

    return invalid_transactions

#-----------------------------------------------------------------------

def generate_report() -> dict:
    """گزارش کامل تراکنش‌های هر کاربر را ایجاد می‌کند."""

    report = {}

    balances = calculate_balance()
    deposits = total_deposits()
    withdrawals = total_withdrawals()
    invalid_transactions = find_invalid_transactions()

    for name in balances:
        report[name] = {
            'name': name,
            'total_deposits': deposits.get(name, 0),
            'total_withdrawals': withdrawals.get(name, 0),
            'balance': balances[name],
            'invalid_transactions': []
        }

    for transaction in invalid_transactions:
        parts = transaction.split(',')
        name = parts[0]

        report[name]['invalid_transactions'].append(transaction)

    return report

#-----------------------------------------------------------------------
## Function calls

report = generate_report()

print('----------------------------------------')
print('          TRANSACTION REPORT')
print('----------------------------------------')

for name in report:

    print()
    print('[', name, ']')
    print('Total deposits    :', report[name]['total_deposits'])
    print('Total withdrawals :', report[name]['total_withdrawals'])
    print('Balance           :', report[name]['balance'])

    print('Invalid transactions:')

    if len(report[name]['invalid_transactions']) == 0:
        print('None')
    else:
        for transaction in report[name]['invalid_transactions']:
            print('-', transaction)

print()
print('----------------------------------------')