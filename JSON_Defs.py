import json
from MainMenu import DATA_FILE

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": {}, "transactions": []}
    except json.JSONDecodeError:
        print("Error: Database file is corrupted.")
        return {"users": {}, "transactions": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
