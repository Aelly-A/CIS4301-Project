with open("../data/loanhistory.sql", "w") as file:
    file.write("DROP TABLE IF EXISTS LoanHistory;\n")