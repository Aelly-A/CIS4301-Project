import helper_functions as helper

def main():
    choice = helper.print_main_menu()
    exit_choice = str(len(helper.MAIN_MENU_OPTIONS))

    while choice != exit_choice: # Main loop
        if choice == "1": # Checkout a Book
            helper.checkout_book()

        elif choice == "2": # Return a Book
            helper.return_book()

        elif choice == "3": # Grant an Extension
            helper.grant_extension()

        elif choice == "4":  # Search a Table
            helper.search_tables()

        elif choice == "5":  # Add a Book
            helper.add_book()

        elif choice == "6":  # Add a User
            helper.add_user()

        elif choice == "7":  # Edit a User
            helper.edit_user()

        elif choice == exit_choice: # Exit
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
