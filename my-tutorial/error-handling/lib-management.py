class BookNotAvailableError(Exception):
    """Exception handling for Book Not Found"""
    def __init__ (self, book_name):
        self.book_name = book_name
    
    def __str__(self):
        return f"The '{self.book_name}' book requested is not available. Request another one!' "

class TooManyRequestedCopiesError(Exception):
    """Exception handling for too many requested copies"""
    def __init__ (self, book_name, available):
        self.book_name = book_name
        self.available = available
    
    def __str__ (self):
        return f"We only have '{self.available} copies of the {self.book_name}'"
    

book_inventory = {
    "Black Box": 5,
    "Sprint": 7,
    "Moments": 4,
    "Articles": 8,
    "Paradox" : 0
}

def borrow_book(name, quantity):
    if name not in book_inventory or book_inventory[name] == 0:
        raise BookNotAvailableError(name)
    elif quantity > book_inventory[name]:
        raise TooManyRequestedCopiesError(name, book_inventory[name])
    else:
        book_inventory[name] -= quantity
        return f"Borrowing successful: {quantity} copies of {name}"

for bk, qty in [("James", 2),("Sprint", 3), ("Paradox", 1)]:
    try:
        print(borrow_book(bk, qty))
    except (BookNotAvailableError, TooManyRequestedCopiesError) as e:
        print(e)
