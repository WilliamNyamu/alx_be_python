class Book:
    total_books = 0
    
    def __init__(self, name):
        self.name = name
        Book.total_books += 1 #Increment for very instance created
    
    @classmethod
    def display_total_books(cls):
        return f"Total number of books created: {cls.total_books}"

book1 = Book("SH")
book2 = Book("Living in the Light")
book3 = Book("Design Principles")
print(Book.display_total_books())