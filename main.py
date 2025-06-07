import helper_functions as helper

def main():
    choice = helper.print_main_menu()
    exit_choice = str(len(helper.MAIN_MENU_OPTIONS))

    while choice != exit_choice:
        if choice == "1": # Checkout
            helper.checkout_book()

        elif choice == "2": # Return
            helper.return_book()

        elif choice == "3": # Grant Extension
            helper.grant_extension()

        elif choice == "4":  # Search Table
            helper.search_tables()

        elif choice == "5":  # Add a book
            helper.add_book()

        elif choice == "6":  # Add a User
            helper.add_user()

        elif choice == "7":  # Edit a User
            helper.edit_user()

        elif choice == exit_choice:
            break

        else:
            print("Choice unrecognised")

        print()
        choice = helper.print_main_menu()

    helper.save_changes()
    print("Successfully saved changes")
    print("Goodbye!")


if __name__ == '__main__':
    main()
