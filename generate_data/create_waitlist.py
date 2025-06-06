from mysql.connector import connect
from random import randint


conn = connect(user="", password="", host="localhost",
               database="library", collation='utf8mb4_unicode_ci')

cur = conn.cursor()

cur.execute("SELECT account_id FROM User;")
account_ids = [x[0] for x in cur.fetchall()]

cur.execute("SELECT isbn FROM Loan")
isbns = [x[0] for x in cur.fetchall()]
print(isbns)



with open("../data/waitlist.sql", "w") as file:
    file.write("DROP TABLE IF EXISTS Waitlist;\n")
    file.write("CREATE TABLE Waitlist(")
    file.write("isbn VARCHAR(16),")
    file.write("account_id VARCHAR(16),")
    file.write("place_in_line INT,")
    file.write("PRIMARY KEY (isbn, account_id));\n")

    waitlist = {}
    for i in range(12):
        user = account_ids[randint(0, len(account_ids) - 1)]
        book = isbns[randint(0, len(isbns) - 1)]

        if randint(0, 3) <= 1 and waitlist:
            book = list(waitlist.keys())[randint(0, len(waitlist) - 1)]
            print(waitlist.keys())
            print(book)

        place_in_line = 1

        if book in waitlist.keys():
            waitlist[book].append(user)
            place_in_line = len(waitlist[book])
        else:
            waitlist[book] = [user]

        file.write(f'INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("{book}", "{user}", {place_in_line});\n')
