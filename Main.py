from MainMenu import MENU_OPTIONS
from users import create_user


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
            case 0:
                create_user()
