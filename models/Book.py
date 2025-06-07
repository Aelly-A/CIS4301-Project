class Book:
    def __init__(self,
                 isbn: str = None,
                 title: str = None,
                 author: str = None,
                 publication_year: str = None,
                 publisher: str = None,
                 total_num_at_branch:int = None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.publisher = publisher
        self.total_num_at_branch = total_num_at_branch

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
        if self.total_num_at_branch != -1:
            self_str += f"Total number of at-branch: {self.total_num_at_branch} \n"

        return self_str

    def __eq__(self, other):
        return self.isbn == other.isbn
