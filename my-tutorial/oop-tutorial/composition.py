class Basic:
    def __init__(self, x = 20, y = 8):
        self.x = x
        self.y = y
    
    def Addition(self):
        return self.x + self.y
    
    def Subtraction(self):
        return self.x - self.y
    
    def Times_table(self):
        for i in range(1, self.y):
            print("%i * %i = %i" % (i, self.y, (i*self.y)))

b = Basic()
b.Addition()
b.Subtraction()
b.Times_table()

class Advanced(Basic):
    def __init__(self, x=20, y=8):
        super().__init__(x, y)

    def Multiply(self):
        return self.x * self.y

a = Advanced()
a.Times_table()

class Comp:
    def __init__(self):
        self.base = Basic()
    
    def Multiply(self):
        return self.base.x * self.base.y

    def Times_y(self):
        return self.base.Times_table()

c = Comp()
print(c.Multiply())
c.Times_y()


class Animal:
    def __init__(self, name = 'Jina', age = '20'):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Generic animal sound")
    
class Dog:
    def __init__(self):
        self.dog = Animal()
    
    def make_sound(self):
        print(f"{self.dog.name} says Woof")

bosco = Dog()
bosco.make_sound()

    