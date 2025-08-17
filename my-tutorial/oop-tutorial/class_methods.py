"""
    Class methods are methods that are bound to the class itself rather than instances of the class (objects). 
    They are used to define methods that operate on class-level data or perform operations related to the class. 
    They are defined using the @classmethod decorator, and the first parameter conventionally named cls represents the class itself.
"""

"""
    When to use class methods:
    1. When you need to access or modify class-specific variables or properties
    2. When you want to create factory methods to create instances of the class
    with specific configurations
"""

class Person:
    count = 0 # Class variable to count instances

    def __init__(self, name):
        self.name = name
        Person.count += 1 # Increment count on instance creation
    
    @classmethod
    def display_count(cls):
        return f"Total persons created: {cls.count}"

# usage
person1 = Person("John")
person2 = Person("Wesley")

# Note: You call the class(Person) and not the instance.
print(Person.display_count())

"""
    Define a class method using the @classmethod decorator.
    Class methods take the class itself, cls, as the first paramter instead of the instance (self)
"""