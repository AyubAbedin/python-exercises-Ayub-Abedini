"""
Created on Wed Sep 16 22:21:58 2026

@author: AA
"""
def check_large_transaction(transaction):
    amount = transaction[2]

    if amount > 100000000:
        return True
    else:
        return False


# Checks if there are more than 3 consecutive withdrawals
def check_repeated_withdrawals(transactions):
    count = {}
    result = []

    for t in transactions:
        name = t[0]
        kind = t[1]

        if name not in count:
            count[name] = 0

        if kind == "withdraw":
            count[name] += 1

            if count[name] > 3:
                result.append(t)
        else:
            count[name] = 0

    return result


# Checks if a withdrawal is greater than the user's balance
def check_balance(transactions):
    balance = {}
    result = []

    for t in transactions:
        name = t[0]
        kind = t[1]
        amount = t[2]

        if name not in balance:
            balance[name] = 0

        if kind == "deposit":
            balance[name] += amount

        elif kind == "withdraw":
            if amount > balance[name]:
                result.append(t)
            else:
                balance[name] -= amount

    return result


# Collects all suspicious transactions
def generate_fraud_report(transactions):
    result = []

    for t in transactions:
        if check_large_transaction(t):
            result.append(t)

    for t in check_repeated_withdrawals(transactions):
        if t not in result:
            result.append(t)

    for t in check_balance(transactions):
        if t not in result:
            result.append(t)

    return result


# Detects suspicious transactions
def detect_fraud(transactions):
    return generate_fraud_report(transactions)


transactions = [ ("Ali", "deposit", 50000000, 10),
                 ("Ali", "withdraw", 2000000, 11),
                 ("Ali", "withdraw", 3000000, 12),
                 ("Ali", "withdraw", 4000000, 13),
                 ("Ali", "withdraw", 5000000, 14),
                 ("Ali", "withdraw", 6000000, 15),
                 ("Sara", "deposit", 50000000, 20),
                 ("Sara", "withdraw", 60000000, 21),
                 ("Reza", "deposit", 150000000, 30)  ]
 

fraud = detect_fraud(transactions)


print("================================")
print("      FRAUD DETECTION REPORT")
print("================================")

print()
print("Suspicious Transactions:")
print("--------------------------------")

for t in fraud:
    print("User:", t[0])
    print("Type:", t[1])
    print("Amount:", t[2])
    print("Transaction ID:", t[3])
    print("--------------------------------")

print("Total suspicious transactions:", len(fraud))
print("================================")