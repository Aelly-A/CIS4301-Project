from mysql.connector import connect, ProgrammingError
from SQL_CREDS import DB_CONFIG

def load_db(username=None, password=None, port="3306", data_dir='data/', verbose=True, parent_cur=None):
    # If you get an error like 'Unknown collation', use the collation argument below.
    # You will also need to make this change in the db_handler file
    try:
        if parent_cur is None:
            conn = connect(user=username, password=password, host="localhost", port=port) # , collation='utf8mb4_unicode_ci')
            cur = conn.cursor()
        else:
            cur = parent_cur

        cur.execute('CREATE DATABASE IF NOT EXISTS library')
        cur.execute('USE library')

        if verbose:
            print()
            print("Connected to the DB")
            print("Inserting Data...")

        filenames = ["book.sql", "user.sql", "loan_history.sql", "loan.sql", "waitlist.sql"]

        for filename in filenames:
            with open(data_dir + filename, "r") as file:
                if verbose:
                    print("Inserting data from", filename)

                for line in file:
                    cur.execute(line)

                if verbose:
                    print("Inserted data from", filename)
                    print()
        if parent_cur is None:
            cur.close()
            conn.commit()
            conn.close()

        return True

    except ProgrammingError as e:
        print()
        print(f"Could not log into the database using")
        print(f"\tUsername: {username}")
        print(f"\tPassword: {password}")
        print(f"\tPort: {port}")
        print()
        print("Error:", e)

        return False


def main():
    data_dir = input("Relative to this directory, where are the sql files (data/ is the default): ")
    if data_dir == "":
        data_dir = "data/"
    elif data_dir[-1] != "/":
        data_dir += "/"

    username = DB_CONFIG["username"]
    password = DB_CONFIG["password"]
    port = DB_CONFIG["port"]

    print(f"\nUsing:\n\tUsername: {username}\n\tPassword: {password}\n\tPort: {port}\n\tData Directory: {data_dir}")

    success = load_db(username=username, password=password, port=port, data_dir=data_dir)
    print()
    if success:
        print("Successfully loaded in the data")
    else:
        print("Failed to insert the data")

if __name__ == "__main__":
    main()