"""
Created on Wed Sep 16 22:37:26 2026

@author: AA
"""

transactions = [ ("Ali", "deposit", 5000000),
                 ("Ali", "withdraw", 1000000),
                 ("Sara", "deposit", 8000000),
                 ("Ali", "withdraw", 500000),
                 ("Sara", "withdraw", 2000000),
                 ("Reza", "deposit", 10000000) ]

def analyze_transactions(transactions: list) -> None:
    """Analyze financial transactions."""
    max_deposit = 0
    max_deposit_user = ""
    max_withdraw = 0
    max_withdraw_user = ""
    max_transactions = 0
    active_user = ""
    result = {}

    for i in transactions:

        if i[0] not in result:
            result[i[0]] = {
                "deposits": 0,
                "withdrawals": 0,
                "balance_change": 0,
                "transactions": 0
            }

        if i[1] == "deposit":
            result[i[0]]["deposits"] += i[2]
            result[i[0]]["balance_change"] += i[2]

        elif i[1] == "withdraw":
            result[i[0]]["withdrawals"] += i[2]
            result[i[0]]["balance_change"] -= i[2]

        result[i[0]]["transactions"] += 1

    for i in result:
        if result[i]["deposits"] > max_deposit:
            max_deposit = result[i]["deposits"]
            max_deposit_user = i

        if result[i]["withdrawals"] > max_withdraw:
            max_withdraw = result[i]["withdrawals"]
            max_withdraw_user = i

        if result[i]["transactions"] > max_transactions:
            max_transactions = result[i]["transactions"]
            active_user = i

    # چاپ اطلاعات کاربران#
    for i in result:
        print("User:", i)
        print("Total deposits:", result[i]["deposits"])
        print("Total withdrawals:", result[i]["withdrawals"])
        print("Balance change:", result[i]["balance_change"])
        print("Number of transactions:", result[i]["transactions"])
        print()

    # چاپ خلاصه#
    print("--- Summary ---")
    print("Highest deposit:", max_deposit_user, max_deposit)
    print("Highest withdrawal:", max_withdraw_user, max_withdraw)
    print("Most active user:", active_user, max_transactions)


analyze_transactions(transactions)