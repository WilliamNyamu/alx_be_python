"""
    Static methods are independent of class instances and the class itself.
    They behave like regular function but are defined inside a class for organization purposes.
    They are defined using the @staticmethod decorator and don't require the self or cls parameter.

    Usage:
    - When a method doesn't need access to class or instance variables (attributes).
    - When you want to group utility functions related to the class within the class definition.

"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
# Usage
print(MathUtils.add(3, 5)) # Output: 8
print(MathUtils.multiply(5, 3)) # Output: 15