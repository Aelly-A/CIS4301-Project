from helper_functions import *

def main():
    choice = print_main_menu()
    exit_choice = str(len(MAIN_MENU_OPTIONS))

    while choice != exit_choice:
        if choice == "1": # Checkout
            checkout_book()

        elif choice == "2": # Return
            return_book()

        elif choice == "3": # Grant Extension
            grant_extension()

        elif choice == "4":  # Search Table
            search_tables()

        elif choice == "5":  # Add a book
            add_book()

        elif choice == "6":  # Add a User
            add_user()

        elif choice == "7":  # Edit a User
            edit_user()

        elif choice == exit_choice:
            break

        else:
            print("Choice unrecognised")

        db.save_changes()
        print()
        choice = print_main_menu()

    db.save_changes()
    print("Successfully saved changes")
    print("Goodbye!")


if __name__ == '__main__':
    main()
