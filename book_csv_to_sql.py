from pandas import read_csv, isna
from random import randint

csv = "Books.csv"
df = read_csv(csv, dtype={'Book-Author': str}, engine='python')
columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Checked-Out"]
used_isbns = []

with open("books.sql", "w") as file:
    file.write("DROP TABLE IF EXISTS Book;\n")
    file.write("DROP TABLE IF EXISTS User;\n")
    file.write("DROP TABLE IF EXISTS Waitlist;\n")
    file.write("DROP TABLE IF EXISTS Loan;\n")
    file.write("DROP TABLE IF EXISTS LoanHistory;\n")

    file.write("CREATE TABLE Book("
               "isbn VARCHAR(16) PRIMARY KEY,"
               "title VARCHAR(256) NOT NULL,"
               "author VARCHAR(128),"
               "publication_year int(4),"
               "publisher VARCHAR(128),"
               "total_num_at_branch INTEGER"
               ");\n")

    for index, row in df.iterrows():
        if isna(row["Book-Author"]) or isna(row["Publisher"]) or isna(row["Year-Of-Publication"]):
            continue

        isbn = row['ISBN']

        title = row['Book-Title'].replace("'", "\\'").replace('"', '\\"')
        author = row['Book-Author'].replace("'", "\\'").replace('"', '\\"')
        publication_year = row['Year-Of-Publication']
        publisher = row['Publisher'].replace("'", "\\'").replace('"', '\\"')
        total_num_at_branch = randint(1, 10)

        file.write(f"INSERT INTO Book (isbn, title, author, publication_year, publisher, total_num_at_branch) VALUES ('{isbn}', '{title}', '{author}', {publication_year}, '{publisher}', {total_num_at_branch});\n")