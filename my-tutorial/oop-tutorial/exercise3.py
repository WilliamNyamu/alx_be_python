class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eat(self):
        return "Eating"
    def sleep(self):
        return "Sleeping"

class Dog(Animal):
    def bark(self):
        return f"{self.name} says 'woof'"

siba = Dog("Siba")
print(siba.bark())
    