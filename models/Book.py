class Book:
    def __init__(self,
                 isbn: str = None,
                 title: str = None,
                 author: str = None,
                 publication_year: str = None,
                 publisher: str = None,
                 num_owned:int = -1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.publisher = publisher
        self.num_owned = num_owned

    def __str__(self):
        self_str = ""

        if self.isbn:
            self_str += f"ISBN: {self.isbn} \n"
        if self.title:
            self_str += f"Title: {self.title} \n"
        if self.author:
            self_str += f"Author: {self.author} \n"
        if self.publication_year:
            self_str += f"Publication year: {self.publication_year} \n"
        if self.publisher:
            self_str += f"Publisher: {self.publisher} \n"
        if self.num_owned != -1:
            self_str += f"Total number of copies owned: {self.num_owned} \n"

        return self_str

    def __eq__(self, other):
        return self.isbn == other.isbn
