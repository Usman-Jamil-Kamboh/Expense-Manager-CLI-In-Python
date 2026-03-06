from MainMenu import MENU_OPTIONS
from finance.users import create_user 
from finance.transections import view_transactions , add_transaction , monthly_report


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

            case 3:
                view_transactions()

            case 4:
                monthly_report()

            case 5:
                  break
            
