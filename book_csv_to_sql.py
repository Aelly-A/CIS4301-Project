from pandas import read_csv, isna
from random import randint

csv = "Books.csv"
df = read_csv(csv, dtype={'Book-Author': str}, engine='python')
columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Checked-Out"]

with open("books.sql", "w") as file:
    file.write("CREATE TABLE Books(\n"
               "\tisbn VARCHAR(16) PRIMARY KEY,\n"
               "\ttitle VARCHAR(256) NOT NULL,\n"
               "\tauthor VARCHAR(128),\n"
               "\tpublication_year int(4),\n"
               "\tpublisher VARCHAR(128),\n"
               "\ttotal_num_at_branch INTEGER\n"
               ");\n\n")

    for index, row in df.iterrows():
        if isna(row["Book-Author"]) or isna(row["Publisher"]) or isna(row["Year-Of-Publication"]):
            continue

        isbn = row['ISBN']
        title = row['Book-Title'].replace("'", "\\'")
        author = row['Book-Author'].replace("'", "\\'")
        publication_year = row['Year-Of-Publication']
        publisher = row['Publisher'].replace("'", "\\'")
        total_num_at_branch = randint(1, 10)

        file.write(f"INSERT INTO Books (isbn, title, author, publication_year, publisher, total_num_at_branch) VALUES ('{isbn}', '{title}', '{author}', {publication_year}, '{publisher}', {total_num_at_branch});\n")