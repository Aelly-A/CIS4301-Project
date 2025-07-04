class Waitlist:
    def __init__(self,
                 isbn: str = None,
                 account_id: str = None,
                 place_in_line: int = -1):
        self.isbn = str(isbn)
        self.account_id = str(account_id)
        self.place_in_line = place_in_line

    def __str__(self):
        self_str = ""
        if self.isbn:
            self_str += f"ISBN: {self.isbn} \n"
        if self.account_id:
            self_str += f"Account ID: {self.account_id} \n"
        if self.place_in_line != -1:
            self_str += f"Place in line: {self.place_in_line} \n"

        return self_str

    def __eq__(self, other):
        return self.account_id == other.account_id and self.isbn == other.isbn
