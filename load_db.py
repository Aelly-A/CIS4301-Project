from mysql.connector import connect, ProgrammingError

def load_db(_username=None, _password=None, _port=None):
    # If you get an error like 'Unknown collation', use the collation argument below
    try:
        conn = connect(user=_username, password=_password, host="localhost", port=_port) # , collation='utf8mb4_unicode_ci')

        cur = conn.cursor()

        cur.execute('DROP DATABASE IF EXISTS library')
        cur.execute('CREATE DATABASE library')
        cur.execute('USE library')

        print("Connected to the DB")

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

        return True

    except ProgrammingError as e:
        print()
        print(f"Could not log into the database using")
        print(f"\tUsername: {_username}")
        print(f"\tPassword: {_password}")
        print(f"\tPort: {_port}")
        print()
        print("Error:", e)

        return False

if __name__ == "__main__":
    username = input("Enter your SQL username: ")
    password = input("Enter your SQL password: ")
    port = input("Enter your SQL port (press enter for the default, 3306): ")

    if port == "":
        port = "3306"

    success = load_db(_username=username, _password=password, _port=port)
    print()
    if success:
        print("Successfully loaded in the data")
    else:
        print("Failed to insert the data")