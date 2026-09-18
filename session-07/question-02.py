# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:02:30 2026

@author: AA
"""
def process_order(customer, *products, **options):
    prices = {
        "Laptop": 1200000,
        "Mouse": 50000,
        "Keyboard": 100000
    }

    discount = options.get("discount", 0)
    tax = options.get("tax", 0)
    shipping = options.get("shipping", 0)

    total_price = 0

    for product in products:
        total_price += prices[product]

    discount_amount = total_price * discount / 100
    price_after_discount = total_price - discount_amount

    tax_amount = price_after_discount * tax / 100

    final_price = price_after_discount + tax_amount + shipping

    result = {
        "customer": customer,
        "products": products,
        "discount": discount,
        "tax": tax,
        "shipping": shipping,
        "final_price": final_price
    }

    return result


result = process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    tax=9,
    shipping=200000
)

print("========== ORDER ==========")
print("Customer:", result["customer"])
print("Products:", result["products"])
print("Discount:", result["discount"], "%")
print("Tax:", result["tax"], "%")
print("Shipping:", result["shipping"])
print("Final Price:", result["final_price"])
print("===========================")