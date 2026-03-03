from MainMenu import MENU_OPTIONS
from finance.users import create_user 
from finance.transections import add_transaction


def show_menu():
    print("\n=== SMART MANAGER ===")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")

while True:
        show_menu()
        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        match choice:
            case 1:
                create_user()

            case 2:
                add_transaction()

            case 5:
                  break
            
