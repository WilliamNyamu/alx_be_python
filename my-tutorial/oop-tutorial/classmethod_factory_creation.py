class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    
    def __str__(self):
        return f"Person(name = '{self.name}', age = '{self.age}')"
    
child = Person.create_child("William")
print(child)