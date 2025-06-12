from mysql.connector import connect

def load_db(_username=None, _password=None, _port=None):
    # If you get an error like 'Unknown collation', use the collation argument below
    conn = connect(user=_username, password=_password, host="localhost", port=_port) # , collation='utf8mb4_unicode_ci')

    cur = conn.cursor()

    print("Connected to database, inserting data...")

    cur.execute('DROP DATABASE IF EXISTS library')
    cur.execute('CREATE DATABASE library')
    cur.execute('USE library')

    for line in open("data/book.sql", "r"):
        cur.execute(line)

    print("Inserted Books")

    for line in open("data/user.sql", "r"):
        cur.execute(line)

    print("Inserted Users")

    for line in open("data/loan_history.sql", "r"):
        cur.execute(line)

    print("Inserted Loan Histories")

    for line in open("data/loan.sql", "r"):
        cur.execute(line)

    print("Inserted Loans")

    for line in open("data/waitlist.sql", "r"):
        cur.execute(line)

    print("Inserted Waitlists")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    username = input("Enter your SQL username: ")
    password = input("Enter your SQL password: ")
    port = input("Enter your SQL port (press enter for the default, 3306): ")

    if port == "":
        port = "3306"

    load_db(_username=username, _password=password, _port=port)