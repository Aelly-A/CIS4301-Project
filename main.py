from db_handler import checkout_book
from helper_functions import *


def main():
    choice = print_main_menu()
    exit_choice = str(len(MAIN_MENU_OPTIONS))

    while choice != exit_choice:
        if choice == "1": # Checkout
            checkout_helper()

        elif choice == "2": # Return
            isbn = input("Enter ISBN: ")
            account_id = input("Enter Account ID: ")

            return_successful = db.return_book(isbn=isbn, account_id=account_id)
            print("Successfully returned") if return_successful else print("Failed to returned")

        elif choice == "3": # Search Book
            search_for_books()

        elif choice == "4":  # Search User
            use_patterns = input("Would you like to use patterns to search String attributes? (Y/N): ").upper() == "Y"
            new_user = User()
            sub_choice = "1"

            while sub_choice != "6" and sub_choice < "7":
                sub_choice = print_filter_user_menu()
                new_user = handle_user_menu_choice(sub_choice, new_user)

            if sub_choice == "6":
                db.get_filtered_users(filter_attributes=new_user, use_patterns=use_patterns)


        elif choice == "5":  # Add a book
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author Name: ")
            publication_year = input("Enter Publication Year: ")
            publisher = input("Enter Publisher: ")
            total_num_at_branch = int(input("Enter Number of Books: "))

            new_book = Book(isbn=isbn, title=title, author=author, publication_year=publication_year,
                            publisher=publisher, total_num_at_branch=total_num_at_branch)

            db.add_book(new_book)

        elif choice == "6":  # Add a User
            account_id = input("Enter Account ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            address = input("Enter Address: ")

            new_user = User(account_id=account_id, name=name, email=email, address=address, phone_number=phone_number)
            db.add_user(new_user=new_user)

            pass

        elif choice == "7":  # Edit a User
            og_account_id = input("Enter OG Account ID: ")
            sub_choice = print_edit_user_menu()
            new_user = User()

            while sub_choice != "6" and sub_choice < "7":
                sub_choice = print_edit_user_menu()
                new_user = handle_user_menu_choice(sub_choice, new_user)

            if sub_choice == "6":
                db.edit_user(original_account_id=og_account_id, new_user=new_user)

        elif choice == exit_choice:
            break

        else:
            print("Choice unrecognised")

        choice = print_main_menu()

    exit_success = db.save_changes()
    print("Successfully saved changes") if exit_success else print("Failed to save changes")
    print("Goodbye!")


if __name__ == '__main__':
    main()