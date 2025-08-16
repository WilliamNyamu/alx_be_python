class Book:
    def __init__(self, title: str, author: str, pages: int):
        # Run validations for the received arguments
        assert isinstance(title, str), f"The book's Title should be a string, received {type(title)} "
        assert isinstance(author, str), f"The book's author should be a string, received {type(author)}"
        assert pages >= 1, f"Pages should be more than 0"


        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__ (self):
        return f"Book(title = '{self.title}', author = '{self.author}, pages = '{self.pages}')"

    def __str__ (self):
        return f"{self.author} wrote '{self.title}' book which has {self.pages} page"

book1 = Book("Money, Sex & Power", "John Piper", 167)
print(book1)
print(repr(book1))
error_book = Book("1984", "William", 1)
print(error_book)