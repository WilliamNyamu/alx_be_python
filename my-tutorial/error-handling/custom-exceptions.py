
# Creating an exception class that inherits from the base Exception class
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    # Initializes the exception with the name of the out-of-stock item.
    def __init__(self, item_name):
        self.item_name = item_name
    
    # Specifies the error message to be displayed when the exception is raised.
    def __str__ (self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
    
#Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0, # Out of Stock
    "grapes": 3
}

# A function to simulate purchasing items from the inventory.

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)
    purchase_item("orange", 1)
    purchase_item("watermelon", 1)
except OutOfStockError as e:
    print(e)