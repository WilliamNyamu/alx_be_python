class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return f"{self.name} is {self.age} years old"

    def __del__ (self):
        print("Bye! Instance destroyed")
        
person1 = Person("William", 20)
print(person1)
    