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
        self_str = ""

        if self.account_id:
            self_str += f"Account ID: {self.account_id} \n"
        if self.name:
            self_str += f"Name: {self.name} \n"
        if self.address:
            self_str += f"Address: {self.address} \n"
        if self.phone_number:
            self_str += f"Phone Number: {self.phone_number} \n"
        if self.email:
            self_str += f"Email: {self.email} \n"

        return self_str

    def __eq__(self, other):
        return self.account_id == other.account_id
