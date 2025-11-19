from unittest import TestCase, main
from datetime import date, timedelta
from importlib import reload
from mariadb import connect

import db_handler as db
from load_db import load_db
from MARIADB_CREDS import DB_CONFIG

from models.Book import Book
from models.User import User


class PublicTests(TestCase):
    # Constructor
    @classmethod
    def setUpClass(cls):
        cls.db = reload(db)
        cls.data_dir = "test_data/"


    # Destructor
    @classmethod
    def tearDownClass(cls):
        load_db(parent_cur=cls.db.cur, parent_conn= cls.db.conn, data_dir=cls.data_dir, verbose=False)
        cls.db.cur.close()
        cls.db.conn.close()


    # Runs before every test
    def setUp(self):
        load_db(parent_cur=self.db.cur, parent_conn= self.db.conn, data_dir=self.data_dir, verbose=False)


    @staticmethod
    def get_book():
        return Book(isbn="0345392876",
                    title="Garfield Dishes It Out (Garfield (Numbered Paperback))",
                    author="Jim Davis",
                    publisher="Ballantine Books",
                    publication_year=1995,
                    num_owned=7)


    @staticmethod
    def get_user() -> User:
        return User(account_id="1d28dd16861b",
                    name="Roberto Martinez",
                    email="roberto-m@yahoo.com",
                    phone_number="324-590-2027",
                    address="4083 SW 91st Blvd, Gainesville, FL 32608")


    def test_add_book(self):
        new_book = self.get_book()
        new_book.isbn ="test_isbn"

        self.db.add_book(new_book=new_book)

        self.db.cur.execute("SELECT isbn, title, author, publication_year, publisher, num_owned "
                         "FROM Book WHERE isbn = %s", (new_book.isbn,))

        inserted_book = self.db.cur.fetchone()

        self.assertEqual(new_book.isbn, inserted_book[0])
        self.assertEqual(new_book.title, inserted_book[1])
        self.assertEqual(new_book.author, inserted_book[2])
        self.assertEqual(new_book.publication_year, inserted_book[3])
        self.assertEqual(new_book.publisher, inserted_book[4])
        self.assertEqual(new_book.num_owned, inserted_book[5])


    def test_edit_user(self):
        new_user = self.get_user()
        new_user.account_id = "test_id"
        original_account_id = "0cf25a005473"

        self.db.edit_user(original_account_id=original_account_id, new_user=new_user)

        self.db.cur.execute("SELECT account_id, name, address, phone_number, email "
                         "FROM User WHERE account_id = %s", (new_user.account_id,))

        edited_user = self.db.cur.fetchone()

        self.db.cur.execute("SELECT account_id, name, address, phone_number, email "
                         "FROM User WHERE account_id = %s", (original_account_id,))

        old_user = self.db.cur.fetchone()

        self.assertIsNone(old_user)

        self.assertEqual(new_user.account_id, edited_user[0])
        self.assertEqual(new_user.name, edited_user[1])
        self.assertEqual(new_user.address, edited_user[2])
        self.assertEqual(new_user.phone_number, edited_user[3])
        self.assertEqual(new_user.email, edited_user[4])


    def test_checkout_book(self):
        random_book = self.get_book().isbn
        random_user = self.get_user().account_id

        self.db.checkout_book(random_book, random_user)

        self.db.cur.execute("SELECT isbn, account_id, checkout_date, due_date FROM Loan WHERE isbn = %s AND account_id = %s", (random_book, random_user))

        inserted_loan = self.db.cur.fetchone()

        checkout_date = date.today().isoformat()
        due_date = (date.today() + timedelta(weeks=2)).isoformat()

        self.assertEqual(random_book, inserted_loan[0])
        self.assertEqual(random_user, inserted_loan[1])
        self.assertEqual(checkout_date, inserted_loan[2].isoformat())
        self.assertEqual(due_date, inserted_loan[3].isoformat())


    def test_waitlist_user(self):
        random_user = "f0bcbb3befe9"
        loaned_book_isbn = "0446389277"

        place_in_line = self.db.waitlist_user(isbn=loaned_book_isbn, account_id=random_user)

        self.assertEqual(1, place_in_line)

        self.db.cur.execute("SELECT isbn, account_id, place_in_line "
                            "FROM Waitlist WHERE isbn = %s AND account_id = %s", (loaned_book_isbn, random_user))

        inserted_waitlist = self.db.cur.fetchone()

        self.assertEqual(loaned_book_isbn, inserted_waitlist[0])
        self.assertEqual(random_user, inserted_waitlist[1])
        self.assertEqual(place_in_line, inserted_waitlist[2])


    def test_update_waitlist(self):
        isbn = "0425042502"

        self.db.update_waitlist(isbn=isbn)

        self.db.cur.execute("SELECT isbn, account_id, place_in_line FROM Waitlist WHERE isbn = %s", (isbn,))

        waitlist = self.db.cur.fetchall()

        for entry in waitlist:
            account_id = entry[1]
            place_in_line = entry[2]
            if account_id == "602cee84a0f2":
                self.assertEqual(1, place_in_line)
            elif account_id == "d9f447e949f8":
                self.assertEqual(2, place_in_line)
            else:
                self.fail("Unexpected account ID")


    def test_return_book(self):
        isbn = "0451521633"
        account_id = "a81fe582ce09"
        checkout_date = (date.today() - timedelta(days=1)).isoformat()
        due_date = (date.today() + timedelta(days=13)).isoformat()
        return_date = date.today().isoformat()

        self.db.return_book(isbn=isbn, account_id=account_id)

        self.db.cur.execute("SELECT isbn, account_id, checkout_date, due_date, return_date "
                            "FROM LoanHistory WHERE isbn = %s AND account_id = %s ", (isbn, account_id))

        loan_history = self.db.cur.fetchone()

        self.assertEqual(isbn, loan_history[0])
        self.assertEqual(account_id, loan_history[1])
        self.assertEqual(checkout_date, loan_history[2].isoformat())
        self.assertEqual(due_date, loan_history[3].isoformat())
        self.assertEqual(return_date, loan_history[4].isoformat())

        self.db.cur.execute("SELECT * FROM Loan WHERE isbn = %s AND account_id = %s", (isbn, account_id))
        self.assertIsNone(self.db.cur.fetchone())


    def test_grant_extension(self):
        isbn = "0486251217"
        account_id = "e64305789806"
        checkout_date = date.today().isoformat()
        new_due_date = (date.today() + timedelta(weeks=4)).isoformat()

        self.db.grant_extension(isbn=isbn, account_id=account_id)

        self.db.cur.execute("SELECT isbn, account_id, checkout_date, due_date "
                            "FROM Loan WHERE isbn = %s AND account_id = %s ", (isbn, account_id))

        loan = self.db.cur.fetchone()

        self.assertEqual(isbn, loan[0])
        self.assertEqual(account_id, loan[1])
        self.assertEqual(checkout_date, loan[2].isoformat())
        self.assertEqual(new_due_date, loan[3].isoformat())


    def test_get_filtered_books(self):
        expected_book = self.get_book()

        results = self.db.get_filtered_books(filter_attributes=expected_book,
                                            min_publication_year=expected_book.publication_year,
                                            max_publication_year=expected_book.publication_year,
                                             use_patterns=False)

        actual_book = results[0]

        self.assertEqual(expected_book.isbn, actual_book.isbn)
        self.assertEqual(expected_book.title, actual_book.title)
        self.assertEqual(expected_book.author, actual_book.author)
        self.assertEqual(expected_book.publication_year, actual_book.publication_year)
        self.assertEqual(expected_book.publisher, actual_book.publisher)
        self.assertEqual(expected_book.num_owned, actual_book.num_owned)


    def test_get_filtered_books_patterns(self):
        expected_book = self.get_book()

        obscured_title = "Garfield % It Out (Ga_field (Nu%red Paperback))"
        obscured_author = "_im_Davis"

        filter_book = Book(title=obscured_title, author=obscured_author)

        results = self.db.get_filtered_books(filter_attributes=filter_book, use_patterns=True)

        actual_book = results[0]

        self.assertEqual(expected_book.isbn, actual_book.isbn)
        self.assertEqual(expected_book.title, actual_book.title)
        self.assertEqual(expected_book.author, actual_book.author)
        self.assertEqual(expected_book.publication_year, actual_book.publication_year)
        self.assertEqual(expected_book.publisher, actual_book.publisher)
        self.assertEqual(expected_book.num_owned, actual_book.num_owned)


    def test_number_in_stock(self):
        isbn = "0312285329"
        expected_num_in_stock = 4

        actual_num_in_stock = self.db.number_in_stock(isbn)

        self.assertEqual(expected_num_in_stock, actual_num_in_stock)


    def test_place_in_line(self):
        isbn = "0425042502"
        account_id = "602cee84a0f2"
        expected_place_in_line = 2

        actual_place_in_line = self.db.place_in_line(isbn=isbn, account_id=account_id)

        self.assertEqual(expected_place_in_line, actual_place_in_line)


    def test_line_length(self):
        isbn = "0425042502"
        expected_line_length = 3
        actual_line_length = self.db.line_length(isbn)

        self.assertEqual(expected_line_length, actual_line_length)


    def test_save_changes(self):
        test_account_id = 'test_id'
        self.db.cur.execute("INSERT INTO User (account_id) VALUES (%s)", (test_account_id,))
        self.db.save_changes()
        self.db.cur.close()
        self.db.conn.close()
        self.db = reload(db)

        self.db.cur.execute("SELECT account_id FROM User WHERE account_id = %s", (test_account_id,))
        result = self.db.cur.fetchone()

        self.assertEqual(test_account_id, result[0])


    def test_close_connection(self):
        temp_conn = connect(user=DB_CONFIG["username"], password=DB_CONFIG["password"], host=DB_CONFIG["host"],
                       database=DB_CONFIG["database"], port=DB_CONFIG["port"])
        temp_cur = temp_conn.cursor()

        temp_cur.execute("SHOW PROCESSLIST")
        process_open = len(temp_cur.fetchall())

        self.db.close_connection()

        temp_cur.execute("SHOW PROCESSLIST")
        process_open_after_close = len(temp_cur.fetchall())

        self.assertEqual(process_open - 1, process_open_after_close)

        self.db = reload(db)


if __name__ == '__main__':
    test = main()
