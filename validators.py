import re

def validate_username(username):
    """
    Username rules:
    - 3 to 15 characters
    - letters, numbers, underscore only
    """
    return re.fullmatch(r"[A-Za-z0-9_]{3,15}", username)

def validate_email(email):

    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)

def validate_amount(amount):
    return re.fullmatch(r"\d+(\.\d{1,2})?", amount)

def validate_date(date):
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", date)
