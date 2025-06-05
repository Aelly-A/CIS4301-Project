from Book import Book
from User import User
import db_handler as db

MAIN_MENU_OPTIONS = [
    "Checkout a Book",
    "Return a Book",
    "Search for a Book",
    "Search for a User",
    "Add a Book",
    "Add a User",
    "Edit a User",
    "Exit"
]

BOOK_OPTIONS = [
    "ISBN",
    "Title",
    "Author",
    "Publisher",
    "Minimum Publication Year",
    "Maximum Publication Year",
    "Continue",
    "Cancel"
]

USER_OPTIONS = [
    "Account ID",
    "Name",
    "Address",
    "Phone Number",
    "Email",
    "Continue",
    "Cancel"
]

def print_menu(menu_header, options):
    print(menu_header)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    print()
    choice = input("Choice: ")
    print()
    return choice


def print_main_menu():
    menu_header = "What would you like to do?"
    return print_menu(menu_header, MAIN_MENU_OPTIONS)


def print_filter_book_menu():
    menu_header = "Which attribute would you like to filter?"
    return print_menu(menu_header, BOOK_OPTIONS)


def print_filter_user_menu():
    menu_header = "Which attribute would you like to filter?"
    return print_menu(menu_header, USER_OPTIONS)


def print_edit_user_menu():
    menu_header = "Which attribute would you like to edit?"
    return print_menu(menu_header, USER_OPTIONS)


def handle_user_menu_choice(choice, new_user=User()):
    if choice == "1":
        new_account_id = input("New Account ID: ")
        new_user.account_id = new_account_id
    elif choice == "2":
        new_name = input("Name: ")
        new_user.name = new_name
    elif choice == "3":
        new_address = input("Address: ")
        new_user.address = new_address
    elif choice == "4":
        new_phone_number = input("Phone Number: ")
        new_user.phone_number = new_phone_number
    elif choice == "5":
        new_email = input("Email: ")
        new_user.email = new_email
    elif choice == "6" or choice == "7":
        return new_user
    else:
        print("Invalid choice")

    print()
    print("Current Attributes:")
    print(new_user.filtered_str())
    print()

    return new_user


def handle_book_menu_choice(choice, new_book=Book()):
    if choice == "1":
        new_isbn = input("ISBN: ")
        new_book.isbn = new_isbn
    elif choice == "2":
        new_title = input("Title: ")
        new_book.title = new_title
    elif choice == "3":
        new_author = input("Author: ")
        new_book.author = new_author
    elif choice == "4":
        new_publisher = input("Publisher: ")
        new_book.publisher = new_publisher
    elif choice in ["5", "6", "7", "8"]:
        return new_book
    else:
        print("Invalid choice")

    return new_book


def search_for_books():
    use_patterns = input("Would you like to use patterns to search String attributes? (Y/N): ").upper() == "Y"
    new_book = Book()
    sub_choice = "1"
    min_pub_year = -1
    max_pub_year = -1

    while sub_choice != "7" and sub_choice != "8":
        sub_choice = print_filter_book_menu()
        new_book = handle_book_menu_choice(sub_choice, new_book)

        try:
            if sub_choice == "5":
                min_pub_year = int(input("Minimum Publication Year: "))
            elif sub_choice == "6":
                max_pub_year = int(input("Maximum Publication Year: "))
        except ValueError:
            print("Please enter a valid integer value")
            print()

        print("Current Attributes:")
        print("--------------------")
        print(new_book.filtered_str(), end="")
        if min_pub_year != -1:
            print(f"Min Publication Year: {min_pub_year}")
        if max_pub_year != -1:
            print(f"Max Publication Year: {max_pub_year}")
        print("--------------------")

    if sub_choice == "8":
        return

    books = db.get_filtered_books(filter_attributes=new_book, use_patterns=use_patterns,
                                  min_publication_year=min_pub_year, max_publication_year=max_pub_year)
    if len(books) == 0:
        print("No books found")
    else:
        print("Found " + str(len(books)) + " book(s):")
        [print(book) for book in books]

def waitlist_user(isbn=None, account_id=None):
    waitlist = input("Would you like to waitlist the User (Y/N): ").upper() == "Y"
    if waitlist == "Y":
        waitlist_successful = db.waitlist_user(isbn=isbn, account_id=account_id)
        print("Successfully waitlisted") if waitlist_successful else print("Failed to waitlist")

def checkout_helper():
    isbn = input("Enter ISBN: ")
    account_id = input("Enter Account ID: ")

    num_available = db.number_in_stock(isbn=isbn)

    if num_available == 0:  # Waitlist
        print("This book is not available right now.")
        waitlist_user(isbn=isbn, account_id=account_id)

    elif num_available == -1:
        print("This library branch does not carry this book.")

    else:
        user_place_in_line = db.place_in_line(isbn=isbn, account_id=account_id)
        people_in_line = db.line_length(isbn=isbn)

        if user_place_in_line == 1 or people_in_line == 0:
            checkout_successful = db.checkout_book(isbn=isbn, account_id=account_id)
            print("Successfully checked out book") if checkout_successful else print("Failed to checked out book")

        else:
            print("User is not next in line to checkout book.")

            if people_in_line > 1:
                waitlist_user(isbn=isbn, account_id=account_id)