import datetime
from JSON_Defs import load_data , save_data
from collections import defaultdict
from math import fsum
from validators import (
    validate_username,
    validate_email,
    validate_amount,
    validate_date
)


def view_transactions():
    data = load_data()

    if not data["transactions"]:
        print("No transactions found.")
        return

    for idx, t in enumerate(data["transactions"], start=1):
        print(
            f"{idx}. {t['user']} | {t['type']} | "
            f"{t['amount']} | {t['category']} | {t['date']}"
        )

def add_transaction():
    data = load_data()

    username = input("Enter username: ")
    if username.lower() not in data["users"]:
        print("User does not exist.")
        return

    amount = input("Enter amount: ")
    if not validate_amount(amount):
        print("Invalid amount.")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format.")
        return

    category = input("Enter category: ")
    t_type = input("Type (income/expense): ").lower()

    if t_type not in ("income", "expense"):
        print("Invalid transaction type.")
        return

    transaction = {
        "user": username,
        "amount": float(amount),
        "date": date,
        "category": category,
        "type": t_type
    }

    data["transactions"].append(transaction)
    save_data(data)
    print("Transaction added successfully.")

def monthly_report():
    data = load_data()
    monthly_totals = defaultdict(list)

    for t in data["transactions"]:
        month = t["date"][:7]
        if t["type"] == "expense":
            monthly_totals[month].append(t["amount"])

    if not monthly_totals:
        print("No expense data available.")
        return

    for month, amounts in monthly_totals.items():
        total = fsum(amounts)
        print(f"{month} → Total Expense: {total}")
