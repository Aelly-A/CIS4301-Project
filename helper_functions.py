import db_handler as db
from models.LoanHistory import LoanHistory
from models.Waitlist import Waitlist
from models.Book import Book
from models.User import User
from models.Loan import Loan

# Basic lists to make menu printing modular
MAIN_MENU_OPTIONS = [
    "Checkout a Book",
    "Return a Book",
    "Grant an Extension",
    "Search a Table",
    "Add a Book",
    "Add a User",
    "Edit a User",
    "Exit"
]

TABLE_OPTIONS = [
    "Book",
    "User",
    "Loan",
    "Loan History",
    "Waitlist",
    "Cancel"
]

# These are used to filter attributes when searching through tables
BOOK_OPTIONS = [ 
    "ISBN",
    "Title",
    "Author",
    "Publisher",
    "Number of Copies Owned",
    "Min Publication Year",
    "Max Publication Year",
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

LOAN_OPTIONS = [
    "ISBN",
    "Account ID",
    "Min Checkout Date",
    "Max Checkout Date",
    "Min Due Date",
    "Max Due Date",
    "Continue",
    "Cancel"
]

WAITLIST_OPTIONS = [
    "ISBN",
    "Account ID",
    "Min Place in line",
    "Max Place in line",
    "Continue",
    "Cancel"
]

LOAN_HISTORY_OPTIONS = [
    "ISBN",
    "Account ID",
    "Min Checkout Date",
    "Max Checkout Date",
    "Min Due Date",
    "Max Due Date",
    "Min Return Date",
    "Max Return Date",
    "Continue",
    "Cancel"
]


# Given a generic list of objects, print them out. The object_name var helps it sound more specific
def print_list_of_objects(objects: list, object_name: str):
    if len(objects) == 0:
        print(f"No {object_name}s found")

    else:
        print(f"Found {str(len(objects))} {object_name}{'s' if len(objects) > 1 else ''}:\n")

        for o in objects:
            print("-" * 20)
            print(str(o)[:-1])
            print("-" * 20)
        

# Generic print menu function
def print_menu(menu_header, options):
    print(menu_header)

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    print()
    choice = input("Choice: ")
    print()

    return choice

# Wrapper functions to simplify menu printing and help code readability
def print_main_menu():
    menu_header = "What would you like to do?"
    return print_menu(menu_header, MAIN_MENU_OPTIONS)

def print_filter_menu(options):
    menu_header = "Which attribute would you like to filter?"
    return print_menu(menu_header, options)


def print_filter_book_menu(): 
    return print_filter_menu(BOOK_OPTIONS)


def print_filter_user_menu():
    return print_filter_menu(USER_OPTIONS)


def print_filter_waitlist_menu():
    return print_filter_menu(WAITLIST_OPTIONS)


def print_filter_loan_menu():
    return print_filter_menu(LOAN_OPTIONS)


def print_filter_loan_history_menu():
    return print_filter_menu(LOAN_HISTORY_OPTIONS)


def print_edit_user_menu():
    menu_header = "Which attribute would you like to edit?"
    return print_menu(menu_header, USER_OPTIONS)


def handle_user_menu_choice(choice, new_user=User()):
    if choice == "1":
        new_account_id = input("Account ID: ")
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
    elif choice not in ["6", "7"]: # Cancel and Continue options
        print("Invalid choice")

    if choice != "7":
        print("Current Attributes:")
        print("--------------------")
        print(new_user, end="")
        print("--------------------")
        print()

    return new_user


def add_book():
    num_owned = 0
    publication_year = -1
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    publisher = input("Enter Publisher: ")

    while publication_year == -1:
        try:
            publication_year = int(input("Enter Publication Year: "))

            if publication_year < 0:
                raise ValueError("Publication Year cannot be negative")

        except ValueError:
            print("Please enter a valid publication year")
            publication_year = -1

        while num_owned == 0:
            try:
                num_owned = int(input("Enter the number of copies that the library owns: "))

                if num_owned < 1:
                    raise ValueError("Number of copies owned cannot be less than one")

            except ValueError:
                print("Please enter a valid number")
                num_owned = 0

    new_book = Book(isbn=isbn, title=title, author=author, publication_year=publication_year,
                    publisher=publisher, num_owned=num_owned)

    db.add_book(new_book)


def add_user():
    account_id = input("Enter Account ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    new_user = User(account_id=account_id, name=name, email=email, address=address, phone_number=phone_number)
    db.add_user(new_user=new_user)


def edit_user():
    og_account_id = input("User's Account ID: ")
    new_user = User()
    choice = '1'

    print()
    while choice != "6" and choice < "7":
        choice = print_edit_user_menu()
        new_user = handle_user_menu_choice(choice, new_user)

    if choice == "6":
        db.edit_user(original_account_id=og_account_id, new_user=new_user)


def waitlist_user(isbn=None, account_id=None):
    waitlist = input("Would you like to waitlist the User (Y/N): ").upper() == "Y"

    if waitlist:
        place_in_line = db.waitlist_user(isbn=isbn, account_id=account_id)

        # Probably a better way to do this, but if it works it works
        last_digit = place_in_line % 10
        num_suffix = "th"
        if last_digit == 1:
            num_suffix = "st"
        elif last_digit == 2:
            num_suffix = "nd"
        elif last_digit == 3:
            num_suffix = "rd"

        print(f"The user is now {place_in_line}{num_suffix} in line to checkout the book")


def checkout_book():
    isbn = input("Enter ISBN: ")
    account_id = input("Enter Account ID: ")

    num_in_stock = db.number_in_stock(isbn=isbn)

    if num_in_stock == 0:  # Out of stock, waitlist the user
        print("This book is not available right now.")
        waitlist_user(isbn=isbn, account_id=account_id)

    elif num_in_stock == -1: # Book not available
        print("This library branch does not carry this book.")

    else: # Check if user is able to check out the book
        user_place_in_line = db.place_in_line(isbn=isbn, account_id=account_id)
        people_in_line = db.line_length(isbn=isbn)

        if user_place_in_line == 1 or people_in_line == 0: # User is either next in line or there is no waitlist
            db.checkout_book(isbn=isbn, account_id=account_id)
            db.update_waitlist(isbn=isbn)
            print("Successfully checked out book")

        else:
            print("User is not next in line to checkout book.")

            if people_in_line > 1 and user_place_in_line == -1: # If the user isn't waitlisted then ask to waitlist them
                waitlist_user(isbn=isbn, account_id=account_id)


def return_book():
    isbn = input("Enter ISBN: ")
    account_id = input("Enter Account ID: ")

    db.return_book(isbn=isbn, account_id=account_id)


def grant_extension():
    isbn = input("Enter ISBN: ")
    account_id = input("Enter Account ID: ")

    db.grant_extension(isbn=isbn, account_id=account_id)


def search_books():
    use_patterns = input("Would you like to use patterns to search String attributes? (Y/N): ").upper() == "Y"
    new_book = Book() # Create an empty book to hold filter attributes
    min_pub_year = -1
    max_pub_year = -1
    choice = "1"

    while choice != "8" and choice != "9":
        choice = print_filter_book_menu()
        try:
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
            elif choice == "4":
                new_num_owned = input("Number of Copies Owned: ")
                new_book.num_owned = new_num_owned
            elif choice == "6":
                min_pub_year = int(input("Min Publication Year: "))
            elif choice == "7":
                max_pub_year = int(input("Max Publication Year: "))
            elif choice not in ["8", "9"]:
                print("Unrecognized choice")
                
        except ValueError:
            print("Please enter a valid integer value")
            print()

        if choice == "9":
            return

        print()
        print("Current Filters:")
        print("--------------------")
        print(new_book, end="")
        if min_pub_year != -1:
            print(f"Min Publication Year: {min_pub_year}")
        if max_pub_year != -1:
            print(f"Max Publication Year: {max_pub_year}")
        print("--------------------")
        print()

    books = db.get_filtered_books(filter_attributes=new_book, use_patterns=use_patterns,
                                  min_publication_year=min_pub_year, max_publication_year=max_pub_year)
    print_list_of_objects(books, "book")
        
        
def search_users():
    use_patterns = input("Would you like to use patterns to search String attributes? (Y/N): ").upper() == "Y"
    new_user = User()
    _choice = "1"

    while _choice != "6" and _choice < "7":
        _choice = print_filter_user_menu()
        new_user = handle_user_menu_choice(_choice, new_user)

    if _choice == "6":
        found_users = db.get_filtered_users(filter_attributes=new_user, use_patterns=use_patterns)

        print_list_of_objects(found_users, "user")


def search_waitlist():
    new_waitlist = Waitlist()
    choice = "1"
    min_place_in_line = -1
    max_place_in_line = -1

    while choice != "5" and choice != "6":
        choice = print_filter_waitlist_menu()
        try:
            if choice == "1":
                new_isbn = input("ISBN: ")
                new_waitlist.isbn = new_isbn
            elif choice == "2":
                new_account_id = input("Account ID: ")
                new_waitlist.account_id = new_account_id
            elif choice == "3":
                min_place_in_line = int(input("Min Publication Year: "))
            elif choice == "4":
                max_place_in_line = int(input("Max Publication Year: "))
            elif choice not in ["5", "6"]:
                print("Unrecognized choice")

        except ValueError:
            print("Please enter a valid integer value")
            print()

        if choice == "6":
            return

        print()
        print("Current Filters:")
        print("--------------------")
        print(new_waitlist, end="")
        if min_place_in_line != -1:
            print(f"Min Place in Line: {min_place_in_line}")
        if max_place_in_line != -1:
            print(f"Max Place in Line: {max_place_in_line}")
        print("--------------------")
        print()

    waitlist_entries = db.get_filtered_waitlist(filter_attributes=new_waitlist, min_place_in_line=min_place_in_line,
                                                max_place_in_line=max_place_in_line)
    print_list_of_objects(waitlist_entries, "waitlisted user")
        

def search_loan():
    new_loan = Loan()
    choice = "1"
    min_checkout_date = ""
    max_checkout_date = ""
    min_due_date = ""
    max_due_date = ""

    while choice != "7" and choice != "8":
        choice = print_filter_loan_menu()

        try:
            if choice == "1":
                new_isbn = input("ISBN: ")
                new_loan.isbn = new_isbn
            elif choice == "2":
                new_account_id = input("Account ID: ")
                new_loan.account_id = new_account_id
            elif choice == "3":
                min_checkout_date = input("Min Checkout Date (YYYY-MM-DD): ")
            elif choice == "4":
                max_checkout_date = input("Max Checkout Date (YYYY-MM-DD): ")
            elif choice == "5":
                min_due_date = input("Max Due Date (YYYY-MM-DD): ")
            elif choice == "6":
                max_due_date = input("Max Due Date (YYYY-MM-DD): ")
            elif choice not in ["7", "8"]:
                print("Unrecognized choice")

        except ValueError:
            print("Please enter a valid integer value")
            print()

        if choice == "8":
            return

        print()
        print("Current Filters:")
        print("--------------------")
        print(new_loan, end="")
        if min_checkout_date:
            print(f"Min Checkout Date: {min_checkout_date}")
        if max_checkout_date:
            print(f"Max Checkout Date: {max_checkout_date}")
        if min_due_date:
            print(f"Min Due Date: {min_due_date}")
        if max_due_date:
            print(f"Max Due Date: {max_due_date}")
        print("--------------------")
        print()

    loans = db.get_filtered_loans(filter_attributes=new_loan, min_checkout_date=min_checkout_date,
                                  max_checkout_date=max_checkout_date, min_due_date=min_due_date,
                                  max_due_date=max_due_date)
    print_list_of_objects(loans, "loan")

def search_loan_history():
    new_loan_history = LoanHistory()
    choice = "1"
    min_checkout_date = ""
    max_checkout_date = ""
    min_due_date = ""
    max_due_date = ""
    min_return_date = ""
    max_return_date = ""

    while choice != "9" and choice != "10":
        choice = print_filter_loan_history_menu()

        try:
            if choice == "1":
                new_isbn = input("ISBN: ")
                new_loan_history.isbn = new_isbn
            elif choice == "2":
                new_account_id = input("Account ID: ")
                new_loan_history.account_id = new_account_id
            elif choice == "3":
                min_checkout_date = input("Min Checkout Date (YYYY-MM-DD): ")
            elif choice == "4":
                max_checkout_date = input("Max Checkout Date (YYYY-MM-DD): ")
            elif choice == "5":
                min_due_date = input("Max Due Date (YYYY-MM-DD): ")
            elif choice == "6":
                max_due_date = input("Max Due Date (YYYY-MM-DD): ")
            elif choice == "7":
                min_return_date = input("Max Return Date (YYYY-MM-DD): ")
            elif choice == "8":
                max_return_date = input("Max Return Date (YYYY-MM-DD): ")
            elif choice not in ["9", "10"]:
                print("Unrecognized choice")

        except ValueError:
            print("Please enter a valid integer value")
            print()

        if choice == "10":
            return

        print()
        print("Current Filters:")
        print("--------------------")
        print(new_loan_history, end="")
        if min_checkout_date:
            print(f"Min Checkout Date: {min_checkout_date}")
        if max_checkout_date:
            print(f"Max Checkout Date: {max_checkout_date}")
        if min_due_date:
            print(f"Min Due Date: {min_due_date}")
        if max_due_date:
            print(f"Max Due Date: {max_due_date}")
        if min_return_date:
            print(f"Min Return Date: {min_return_date}")
        if max_return_date:
            print(f"Max Return Date: {max_return_date}")
        print("--------------------")
        print()

    loans = db.get_filtered_loan_histories(filter_attributes=new_loan_history, min_checkout_date=min_checkout_date,
                                           max_checkout_date=max_checkout_date, min_due_date=min_due_date,
                                           max_due_date=max_due_date, min_return_date=min_return_date,
                                           max_return_date=max_return_date)
    print_list_of_objects(loans, "return")


def search_tables():
    choice = print_menu("Which table would you like to search?", TABLE_OPTIONS)

    if choice == "1":
        search_books()
    elif choice == "2":
        search_users()
    elif choice == "3":
        search_loan()
    elif choice == "4":
        search_loan_history()
    elif choice == "5":
        search_waitlist()
    elif choice == "6":
        return
    else:
        print("Invalid choice")


def save_changes():
    db.save_changes()


def close_connection():
    db.close_connection()
