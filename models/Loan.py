class Loan:
    def __init__(self,
                 isbn: str = None,
                 account_id: str = None,
                 checkout_date: str = None,
                 due_date: str = None):
        self.isbn = isbn
        self.account_id = account_id
        self.checkout_date = checkout_date
        self.due_date = due_date

    def __str__(self):
        self_str = ""

        if self.isbn:
            self_str += f"ISBN: {self.isbn} \n"
        if self.account_id:
            self_str += f"Account ID: {self.account_id} \n"
        if self.checkout_date:
            self_str += f"Checkout Date: {self.checkout_date} \n"
        if self.due_date:
            self_str += f"Due Date: {self.due_date} \n"

        return self_str

    def __eq__(self, other):
        return self.account_id == other.account_id and self.isbn == other.isbn
