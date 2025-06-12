from mysql.connector import connect
from datetime import date, timedelta
from random import randint
from models.Book import Book
from math import floor

def daterange(_start_date: date, _end_date: date):
    days = int((_end_date - _start_date).days)
    for n in range(days):
        yield _start_date + timedelta(n)

def convert_db_book_to_book_object(rows=None) -> list[Book]:
    _books = []

    for row in rows:
        isbn = row[0]
        title = row[1]
        author = row[2]
        pub_year = row[3]
        publisher = row[4]
        num_at_branch = row[5]
        _books.append(Book(isbn=isbn,
                          title=title,
                          author=author,
                          publication_year=pub_year,
                          publisher=publisher,
                          total_num_at_branch=num_at_branch))

    return _books

conn = connect(user="", password="", host="localhost",
               database="library", collation='utf8mb4_unicode_ci')

cur = conn.cursor()

cur.execute("SELECT account_id FROM User;")
account_ids = [x[0] for x in cur.fetchall()]

cur.execute("SELECT isbn, title, author, publication_year, publisher, total_num_at_branch FROM Book")
books = convert_db_book_to_book_object(cur.fetchall())

start_date = date(2020, 9, 12)
end_date = date(2025, 3, 25)

TWO_WEEKS = timedelta(weeks=2)

with open("../data/loan_history.sql", "w") as file:
    file.write("DROP TABLE IF EXISTS LoanHistory;\n")
    file.write("CREATE TABLE LoanHistory(")
    file.write("isbn VARCHAR(16),")
    file.write("account_id VARCHAR(16),")
    file.write("checkout_date DATE, ")
    file.write("due_date DATE NOT NULL,")
    file.write("return_date DATE NOT NULL,")
    file.write("PRIMARY KEY (isbn, account_id, checkout_date));\n")

    for single_date in daterange(start_date, end_date):
        number_of_checkouts = randint(-22, 10)
        if number_of_checkouts < 1:
            continue
        number_of_checkouts = floor(number_of_checkouts ** 0.5)

        for i in range(number_of_checkouts):
            user = account_ids[randint(0, len(account_ids) - 1)]
            book = books[randint(0, len(books) - 1)]
            while int(book.publication_year) > single_date.year:
                book = books[randint(0, len(books) - 1)]

            due_date = single_date + TWO_WEEKS
            if randint(0, 6) > 4:
                due_date += TWO_WEEKS
            late = randint(0, 5)

            rand_end = timedelta(randint(0, int((due_date - single_date).days) + late))

            return_date = (single_date + rand_end).strftime("%Y-%m-%d")
            checkout_date = single_date.strftime("%Y-%m-%d")
            due_date = due_date.strftime("%Y-%m-%d")

            file.write(f'INSERT INTO LoanHistory (isbn, account_id, checkout_date, due_date, return_date) VALUES ("{book.isbn}", "{user}", "{checkout_date}", "{due_date}", "{return_date}");\n')
