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
        print("-" * 20 + "\n" +
        f"ISBN: {self.isbn}\n" +
        f"Title: {self.title}\n" +
        f"Author: {self.author}\n" +
        f"Publication Year: {self.publication_year}\n" +
        f"Publisher: {self.publisher}\n" +
        f"Total Num at Branch: {self.total_num_at_branch}\n" +
        "-" * 20)
        
    def filtered_str(self):
        return ((f"ISBN: {self.isbn}\n" if self.isbn else "") +
              (f"Title: {self.title}\n" if self.title else "") +
              (f"Author: {self.author}\n" if self.author else "") +
              (f"Publication Year: {self.publication_year}\n" if self.publication_year else "") +
              (f"Publisher: {self.publisher}\n" if self.publisher else "") +
              (f"Total Num at Branch: {self.total_num_at_branch}\n" if self.total_num_at_branch else ""))

    def __eq__(self, other):
        return self.isbn == other.isbn
