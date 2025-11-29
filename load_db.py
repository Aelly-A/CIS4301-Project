from mariadb import connect, ProgrammingError
from MARIADB_CREDS import DB_CONFIG

def load_db(data_dir='data/', verbose=True, parent_cur=None, parent_conn=None):
    # If you get an error like 'Unknown collation', use the collation argument in line 16.
    # You will also need to make this change in the db_handler file
    try:
        # parent_cur and conn are only needed to run the tests and not have multiple connections to the DB.
        if parent_cur is None and parent_conn is None:
            username = DB_CONFIG["username"]
            password = DB_CONFIG["password"]
            host= DB_CONFIG["host"]
            port = DB_CONFIG["port"]

            print(f"\nUsing:\n\tUsername: {username}\n\tPassword: {password}\n\tPort: {port}\n\tData Directory: {data_dir}")

            conn = connect(username=username, password=password, host=host, port=port) # , collation='utf8mb4_unicode_ci')
            cur = conn.cursor()
        else:
            cur = parent_cur

        database = DB_CONFIG["database"]
        cur.execute('CREATE DATABASE IF NOT EXISTS ?', database)
        cur.execute('USE ?', database)

        if verbose:
            print()
            print("Connected to the DB")
            print("Inserting Data...")

        filenames = ["book.sql", "user.sql", "loan_history.sql", "loan.sql", "waitlist.sql"]

        # Run through all the data files and execute them line by line
        for filename in filenames:
            with open(data_dir + filename, "r") as file:
                if verbose:
                    print("Inserting data from", filename)

                # The second argument is due to MariaDB using '?' as a placeholder, so we're saying put ? in its place
                for line in file:
                    cur.execute(line, ["?"] * line.count("?"))

        if verbose:
            print("Inserted data from", filename)
            print()

        if parent_cur is None and parent_conn is None:
            cur.close()
            conn.commit()
            conn.close()

        else:
            parent_conn.commit()

    # Some SQL error, could be bad login or something else
    except ProgrammingError as e:
        if verbose:
            print("Error:", e)

        return False

    # Case if data_dir is bad
    except FileNotFoundError:
        if verbose:
            print(f"Could not find directory {data_dir}. Please make sure you use tha path relative to CIS4301-Project.")
            print(f"So for example, this file is ./load_db.py")

    return True


def main():
    data_dir = input("What directory contains the sql files you wish to load in (data/ is the default): ").strip()
    if data_dir == "":
        data_dir = "data/"
    elif data_dir[-1] != "/":
        data_dir += "/"

    success = load_db(data_dir=data_dir)

    if success:
        print("Successfully loaded in the data")
    else:
        print("Failed to insert the data")

if __name__ == "__main__":
    main()