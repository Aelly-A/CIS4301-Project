from mysql.connector import connect, ProgrammingError

def load_db(_username=None, _password=None, _port="3306", _data_dir='data/', verbose=True):
    # If you get an error like 'Unknown collation', use the collation argument below.
    # You will also need to make this change in the db_handler file
    try:
        conn = connect(user=_username, password=_password, host="localhost", port=_port) # , collation='utf8mb4_unicode_ci')

        cur = conn.cursor()

        cur.execute('CREATE DATABASE IF NOT EXISTS library')
        cur.execute('USE library')

        if verbose:
            print()
            print("Connected to the DB")
            print("Inserting Data...")

        filenames = ["book.sql", "user.sql", "loan_history.sql", "loan.sql", "waitlist.sql"]

        for filename in filenames:
            with open(_data_dir + filename, "r") as file:
                if verbose:
                    print("Inserting data from", filename)

                for line in file:
                    cur.execute(line)

                if verbose:
                    print("Inserted data from", filename)
                    print()

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
    port = input("Enter your SQL port (3306 is the default): ")
    data_dir = input("Relative to this directory, where are the sql files (data/ is the default): ")

    if port == "":
        port = "3306"

    if data_dir == "":
        data_dir = "data/"
    elif data_dir[-1] != "/":
        data_dir += "/"

    print(f"\nUsing:\n\tUsername: {username}\n\tPassword: {password}\n\tPort: {port}\n\tData Directory: {data_dir}")

    success = load_db(_username=username, _password=password, _port=port, _data_dir=data_dir)
    print()
    if success:
        print("Successfully loaded in the data")
    else:
        print("Failed to insert the data")