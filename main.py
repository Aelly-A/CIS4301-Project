import helper_functions as helper

def main():
    choice = helper.print_main_menu() # Leaving the input as str so there won't be a type error when converting to int
    exit_choice = "8"

    # Dictionary to convert user input into a function
    top_level_functions = {
        "1": helper.checkout_book,
        "2": helper.return_book,
        "3": helper.grant_extension,
        "4": helper.search_tables,
        "5": helper.add_book,
        "6": helper.add_user,
        "7": helper.edit_user,
    }

    # Dictionary to convert user input into a function
    top_level_functions = {
        "1": helper.checkout_book,
        "2": helper.return_book,
        "3": helper.grant_extension,
        "4": helper.search_tables,
        "5": helper.add_book,
        "6": helper.add_user,
        "7": helper.edit_user,
    }

    # Main loop
    while choice != exit_choice:
        if choice in top_level_functions.keys():
            top_level_functions[choice]() # Get the func from the dictionary and run it

        else:
            print("Choice unrecognised")

        helper.save_changes() # Save changes after an iteration
        print()
        choice = helper.print_main_menu()

    helper.close_connection() # Safely close the connection
    print("Successfully saved changes, Goodbye!")
    print()


if __name__ == '__main__':
    main()
