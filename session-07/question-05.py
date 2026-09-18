# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:47:42 2026

@author: AA
"""

logs = [ ("Ali", "LOGIN", 200),
        ("Ali", "DOWNLOAD", 200),
        ("Sara", "LOGIN", 403),
        ("Reza", "LOGIN", 200),
        ("Sara", "LOGIN", 403),
        ("Sara", "LOGIN", 403) ]


# Counts successful logins
def count_successful_logins(logs: list) -> int:
    """Count successful logins."""
    count = 0

    for i in logs:
        if i[1] == "LOGIN" and i[2] == 200:
            count += 1

    return count


# Counts failed logins
def count_failed_logins(logs: list) -> int:
    """Count failed logins."""
    count = 0

    for i in logs:
        if i[1] == "LOGIN" and i[2] == 403:
            count += 1

    return count


# Finds suspicious users
def find_suspicious_users(logs: list) -> list:
    """Find users with repeated failed logins."""
    count = {}
    result = []

    for i in logs:
        name = i[0]
        status = i[2]

        if i[1] == "LOGIN" and status == 403:
            if name not in count:
                count[name] = 0

            count[name] += 1

    for name in count:
        if count[name] >= 3:
            result.append(name)

    return result


# Counts operations for each user
def count_user_operations(logs: list) -> dict:
    """Count operations for each user."""
    count = {}

    for i in logs:
        name = i[0]

        if name not in count:
            count[name] = 0

        count[name] += 1

    return count


# Generates the final report
def generate_report(logs: list) -> dict:
    """Generate the final log report."""
    result = {}

    result["successful_logins"] = count_successful_logins(logs)
    result["failed_logins"] = count_failed_logins(logs)
    result["suspicious_users"] = find_suspicious_users(logs)
    result["user_operations"] = count_user_operations(logs)

    return result


# Runs the program
report = generate_report(logs)


# Prints the final report
print("========== LOG ANALYSIS ==========")
print()

print("Successful Logins :", report["successful_logins"])
print("Failed Logins     :", report["failed_logins"])

print()
print("Suspicious Users")
print("----------------")

for name in report["suspicious_users"]:
    print(name, "-> 3 failed logins")

print()
print("User Operations")
print("---------------")

for name in report["user_operations"]:
    print(name, "->", report["user_operations"][name], "operations")

print()
print("==================================")