from JSON_Defs import load_data, save_data
from validators import (
    validate_username,
    validate_email,
    validate_amount,
    validate_date
)
from datetime import datetime

def create_user():
    data = load_data()

    username = input("Enter username: ")
    if not validate_username(username):
        print("Invalid username format.")
        return

    if username in data["users"]:
        print("User already exists.")
        return

    email = input("Enter email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return

    data["users"][username.lower()] = {
        "email": email,
        "created_at": datetime.now().isoformat()
    }

    save_data(data)
    print("User created successfully.")
