
class Item:
    # Create a class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # Collects all instances
    def __init__ (self, name: str, price: float, quantity = 0): # Serve as documentation for type hints(annotations). name: str is a hint, not an enforcement
        # Run validation to the received arguments
        # Enforce rules on the receives arguments before working on them.
        assert price >= 0, f"Price '{price}' is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity '{quantity}' is not greater or equal to zero"
        assert isinstance(name, str), f"Name must be a string, got {name}"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    def item_name(self):
        return self.name

    def calculate_total_price(self):
        return f"{self.item_name()} is {self.price * self.quantity}"
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        pass
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"




print(Item.all)
Item.instantiate_from_csv()


# item1 = Item("Phone", 100, 1)
# print(item1.calculate_total_price())

# # # __dict__ is a magic attribute that shows the attributes of a class or instance
# # print(Item.__dict__) # Brings all the attribute for the Class level
# # print(item1.__dict__) # Brings all the attributes for the object level

# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# print(item2.apply_discount())

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Kepboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)





