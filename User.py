class User:
    def __init__(self,
                 account_id: str = None,
                 name: str = None,
                 address: str = None,
                 phone_number: str = None,
                 email: str = None):
        self.account_id = account_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        self_str = ("-" * 20 + "\n" +
                    f"Account ID: {self.account_id}\n" +
                    f"Name: {self.name}\n" +
                    f"Address: {self.address}\n" +
                    f"Phone Number: {self.phone_number}\n" +
                    f"Email: {self.email}\n" +
                    "-" * 20)

        return self_str


    def filtered_str(self):
        self_str = ("-" * 20 + "\n" +
                    (f"Account ID: {self.account_id}\n" if self.account_id else "") +
                    (f"Name: {self.name}\n" if self.name else "") +
                    (f"Address: {self.address}\n" if self.address else "") +
                    (f"Phone Number: {self.phone_number}\n" if self.phone_number else "") +
                    (f"Email: {self.email}\n" if self.email else "") +
                    "-" * 20)

        return self_str
    def print_user(self):
        print(self)

    def __eq__(self, other):
        return self.account_id == other.account_id
