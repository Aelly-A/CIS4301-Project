from mysql.connector import connect
from models.LoanHistory import LoanHistory
from models.Waitlist import Waitlist
from models.Book import Book
from models.User import User
from models.Loan import Loan

DB_CONFIG = {
    "user": "username",
    "password": "password",
    "host": "localhost",
    "database": "library",
}

conn = connect(user=DB_CONFIG["user"], password=DB_CONFIG["password"], host=DB_CONFIG["host"],
               database=DB_CONFIG["database"], collation='utf8mb4_unicode_ci')

cur = conn.cursor()

"""
filter_attributes - A Book object containing attributes to filter books in the database. If an attribute is None 
    then it should not be considered for the search. e.g. if filter_attributes.title = "1984" then all books returned 
    should have their title == "1984". If filter_attributes.author = None then we do not care what the author is, when 
    filtering. It is important to note that filter_attributes.publication_year will always be None since we have
    separate parameters to handel publication_year.
use_patterns - If True, then the string attributes in filter_attributes may contain string patterns rather than typical 
    string literals, so the filtering should handle this accordingly. e.g. if filter_attributes.title = "The Great%" and 
    use_patterns = True, then all Books returned should have their title start with "The Great%". If use_patterns = False
    then all books returned should have their title == "The Great%".
min_publication_year - The minimum publication year to filter books by, inclusively. e.g. if min_publication_year = 2000,
    then all books should be published between 2000 and the current year, including 2000 and the current year 
max_publication_year - The maximum publication year to filter books by, inclusively. e.g. if max_publication_year = 1990,
    then all books should be published before the year 2000, not including 2000.

returns a list of Book objects with books that meet the qualifications of the filtered attributes. If no books meet the 
    requirements, then an empty list is returned
"""
def get_filtered_books(filter_attributes: Book = None,
                       use_patterns: bool = False,
                       min_publication_year: int = None,
                       max_publication_year: int = None) -> list[Book]:
    return []

"""
filter_attributes - A User object containing attributes to filter users in the database. If an attribute is None 
    then it should not be considered for the search. e.g. if filter_attributes.name = "John" then all users returned 
    should have their name == "John". If filter_attributes.address = None then we do not care what the address is, when 
    filtering.
use_patterns - If True, then the string attributes in filter_attributes may contain string patterns rather than typical 
    string literals, so the search should handle this accordingly. e.g. if filter_attributes.name = "John%" and 
    use_patterns = True, then all Users returned should have their name start with "John". If use_patterns = False then
    all users returned should have their name == "John%".
    
returns a list of User objects with users who meet the qualifications of the filtered attributes. If no users meet the 
    requirements, then an empty list is returned
"""
def get_filtered_users(filter_attributes: User = None,
                       use_patterns: bool = False) -> list[User]:
    return []


"""
filter_attributes - A User object containing attributes to filter users in the database. If an attribute is None 
    then it should not be considered for the search. e.g. if filter_attributes.name = "John" then all users returned 
    should have their name == "John". If filter_attributes.address = None then we do not care what the address is, when 
    filtering.
use_patterns - If True, then the string attributes in filter_attributes may contain string patterns rather than typical 
    string literals, so the search should handle this accordingly. e.g. if filter_attributes.name = "John%" and 
    use_patterns = True, then all Users returned should have their name start with "John". If use_patterns = False then
    all users returned should have their name == "John%".
min_checkout_date - The minimum checkout date (formatted in YYYY-mm-dd) to filter loans by, inclusively. e.g. if min_checkout_date = "2025-01-02",
    then all loans should be checked out after "2025-01-01", not including "2025-01-01".
max_checkout_date - The maximum checkout date (formatted in YYYY-mm-dd) to filter loans by, inclusively. e.g. if max_checkout_date = "2025-01-02",
    then all loans should be checked out before "2025-01-03", not including "2025-01-03"
min_due_date - like min_checkout_date but with the due date instead
max_due_date - like max_checkout_date but with the due date instead

returns a list of Loan objects with loans that meet the qualifications of the filtered attributes. If no loans meet the 
    requirements, then an empty list is returned
"""
def get_filtered_loans(filter_attributes: Loan = None,
                       use_patterns: bool = False,
                       min_checkout_date: str = None,
                       max_checkout_date: str = None,
                       min_due_date: str = None,
                       max_due_date: str = None,) -> list[Loan]:
    return []


"""
filter_attributes - A User object containing attributes to filter users in the database. If an attribute is None 
    then it should not be considered for the search. e.g. if filter_attributes.name = "John" then all users returned 
    should have their name == "John". If filter_attributes.address = None then we do not care what the address is, when 
    filtering.
use_patterns - If True, then the string attributes in filter_attributes may contain string patterns rather than typical 
    string literals, so the search should handle this accordingly. e.g. if filter_attributes.name = "John%" and 
    use_patterns = True, then all Users returned should have their name start with "John". If use_patterns = False then
    all users returned should have their name == "John%".
min_checkout_date - The minimum checkout date (formatted in YYYY-mm-dd) to filter loans by, inclusively. e.g. if min_checkout_date = "2025-01-02",
    then all loans should be checked out after "2025-01-01", not including "2025-01-01".
max_checkout_date - The maximum checkout date (formatted in YYYY-mm-dd) to filter loans by, inclusively. e.g. if max_checkout_date = "2025-01-02",
    then all loans should be checked out before "2025-01-03", not including "2025-01-03"
min_due_date - like min_checkout_date but with the due date instead
max_due_date - like max_checkout_date but with the due date instead
min_return_date - like min_checkout_date but with the return date instead
max_return_date - like max_checkout_date but with the return date instead

returns a list of LoanHistory objects with Loan History entries that meet the qualifications of the filtered attributes.
    If no entries meet the requirements, then an empty list is returned
"""
def get_filtered_loan_histories(filter_attributes: LoanHistory = None,
                                use_patterns: bool = False,
                                min_checkout_date: str = None,
                                max_checkout_date: str = None,
                                min_due_date: str = None,
                                max_due_date: str = None,
                                min_return_date: str = None,
                                max_return_date: str = None) -> list[LoanHistory]:
    return []


"""
filter_attributes - A User object containing attributes to filter users in the database. If an attribute is None 
    then it should not be considered for the search. e.g. if filter_attributes.name = "John" then all users returned 
    should have their name == "John". If filter_attributes.address = None then we do not care what the address is, when 
    filtering.
use_patterns - If True, then the string attributes in filter_attributes may contain string patterns rather than typical 
    string literals, so the search should handle this accordingly. e.g. if filter_attributes.name = "John%" and 
    use_patterns = True, then all Users returned should have their name start with "John". If use_patterns = False then
    all users returned should have their name == "John%".
min_place_in_line - The minimum place in line for a waitlist to be. e.g. if min_place_in_line = 3 then only entries 
    where the place_in_line is greater than or equal to 3 should be included.
max_place_in_line - The minimum place in line for a waitlist to be. e.g. if max_place_in_line = 3 then only entries 
    where the place_in_line is less than or equal to 3 should be included.
    
returns a list of Waitlist objects with waitlist entries that meet the qualifications of the filtered attributes. 
    If no entries meet the requirements, then an empty list is returned
"""
def get_filtered_waitlist(filter_attributes: Waitlist = None,
                          use_patterns: bool = False,
                          min_place_in_line: int = -1,
                          max_place_in_line: int = -1) -> list[Waitlist]:
    return []

"""
isbn - A string containing the ISBN for a book to get from the DB. e.g. if isbn = "0375759778", then the Book object 
    returned should contain all the information from that book in the DB.

returns a Book object containing the book that is retrieved from the DB. If no book is found in the DB then return None.  
"""
def get_book(isbn: str = None) -> Book:
    return Book()

"""
new_book - A Book object containing a new book to be inserted into the DB in the Books table. 

returns a bool that should be True if the book was inserted successfully, and False if the book was not inserted.
"""
def add_book(new_book: Book = None) -> bool:
    return True

"""
new_user - A User object containing a new user to be inserted into the DB in the Users table. 

returns a bool that should be True if the user was inserted successfully, and False if the user was not inserted.
"""
def add_user(new_user: User = None) -> bool:
    return True

"""
original_account_id - A string containing the account id for the user to be edited. e.g. if the original_account_id =
    "0375759778", then all attributes that are being updated should be applied to the user in the DB with account_id ==  
    "0375759778".
     
new_user - A User object containing attributes to update for a user in the database. If an attribute is None 
    then it should not be altered. e.g. if new_user.name = "John" then the user with the same account_id as 
    original_account_id should have their name updated to "John". If filter_attributes.name = None, then the name should
    not be altered. 

returns a bool that should be True if the user was updated successfully, and False if the user was not updated.
"""
def edit_user(original_account_id: str = None,
              new_user: User = None) -> bool:
    return True

# Returns a bool showing success of save changes operation
def save_changes() -> bool:
    return True

"""
isbn - A string containing the ISBN for a book.

returns a bool that should be True if a book in the DB has the same ISBN as the isbn parameter, False otherwise
"""
def book_exists(isbn: str = None) -> bool:
    return True

"""
isbn - A string containing the ISBN for a book.

returns the quantity of books available with their ISBN equal to the isbn parameter. The quantity available should be 
    calculated as how copies the branch owns minus how many copies are checked out to users. If the library does not 
    have the book then -1 should be returned.
"""
def number_in_stock(isbn: str = None) -> int:
    return 0

"""
isbn - A string containing the ISBN for the book that a user desires to check out.
account_id - A string containing the account id for the user that wants to check out the book.
checkout_date - A string containing the date the book was checked out, formatted in YYYY-mm-dd. e.g. January 2nd, 2000
    would be 2000-01-02
due_date - A string containing the date the book is supposed to be returned, formatted in YYYY-mm-dd. e.g. January 2nd, 
    2000 would be 2000-01-02
    
returns bool which is True if the user is successfully able to check out the book, and False otherwise. When checking
    out a book a new record should be inserted into the Loan table. It is important to note that the waitlist table 
    should not be altered in this function, as it will updated separately in the update_waitlist function. 
"""
def checkout_book(isbn: str = None,
                  account_id: str = None,
                  checkout_date: str = None,
                  due_date: str = None) -> bool:
    return True


"""
isbn - A string containing the ISBN for a book on the waitlist

returns a bool that is true if the waitlist is successfully updated, and False otherwise. To successfully update the 
    waitlist, the user who is next inline to receive the book should be removed from the waitlist, and all other users 
    waiting on the same book should move forward a place in line.
"""
def update_waitlist(isbn: str = None) -> bool:
    return True


"""
isbn - A string containing the ISBN for the book that a user desires to be waitlisted for.
account_id - A string containing the account id for the user that wants to be waitlisted.

returns bool which is True if the user is successfully able to be waitlisted for the book, and False otherwise. When
    a user is waitlisted a new record should be inserted into the Waitlist table. Adding the user to the waitlist should
    put them in the last place in line to receive the book.
"""
def waitlist_user(isbn: str = None,
                  account_id: str = None) -> bool:
    return True

"""
isbn - A string containing the ISBN for the book that the user desires to return.
account_id - A string containing the account id for the user that wants to return the book.
return_date - A string containing the date the book was returned, formatted in YYYY-mm-dd. e.g. January 2nd, 2000
    would be 2000-01-02
    
returns bool which is True if the user is successfully able to return the book, and False otherwise. When returning a 
    book, all that is needed is to delete the corresponding entry from the Loan table, and insert a new record into the
    Loan_history.
"""
def return_book(isbn: str = None,
                account_id: str = None,
                return_date: str = None) -> bool:
    return True

"""
isbn - A string containing the ISBN for a book
account_id - A string containing the account id for a user

returns what place in line the user with the corresponding account_id is in for the book with the corresponding ISBN. If
    the user is not on the waitlist for that book then return -1
"""
def place_in_line(isbn: str = None,
                  account_id: str = None) -> int:
    return 1

"""
isbn - A string containing the ISBN for a book

returns how many people are on the waitlist for the book with the corresponding ISBN. e.g. if there are 5 people on the
 waitlist for a book, 5 should be returned. If the book is not on the waitlist, then 0 should be returned.
"""
def line_length(isbn: str = None)-> int:
    return 0

"""
isbn - A string containing the ISBN for a book
account_id - A string containing the account id for a user
new_due_date - The date that the book is now due, formatted in YYYY-mm-dd

returns a bool showing whether the user was granted an extension or not

"""
def grant_extension(isbn: str = None,
                    account_id: str = None,
                    new_due_date: str = None) -> bool:
    return True