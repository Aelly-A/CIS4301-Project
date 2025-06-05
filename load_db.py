from mysql.connector import connect

if __name__ == "__main__":
    username = input("Enter your SQL username: ")
    password = input("Enter your SQL password: ")
    port = input("Enter your SQL port (press enter for the default, 3306): ")

    if port == "":
        port = "3306"

    conn = connect(user=username, password=password, host="localhost", database="library",
                   collation='utf8mb4_unicode_ci', port=port)

    cur = conn.cursor()

    for line in open("data/book.sql", "r"):
        cur.execute(line)

    for line in open("data/user.sql", "r"):
        cur.execute(line)

    conn.commit()
    conn.close()