class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default attribute value

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# The __init__ method (constructor) initializes attributes like make

# You can create object (instances) of the Car class and access
# its methods and attributes as follows:

my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descriptive_name()) # Output: 2020 Toyota Camry

my_car.read_odometer()
my_car.update_odometer(100)
my_car.read_odometer()

my_car.increment_odometer(50)
my_car.read_odometer()

class Student:
    def __init__(self, name, age, maths, english):
        self.name = name
        self.age = age
        self.maths = maths
        self.english = english

    def student_info(self):
        return f"Hello, {self.name}. What do you want to learn at your {self.age}?"
    
    def calculate(self):
        global marks
        marks = self.maths + self.english
        return marks
    def grade(self):
        if marks >= 190:
            grade = "A"
        elif marks >= 170:
            grade = "B"
        elif marks >= 150:
            grade = "C"
        else:
            grade = "D"

        return grade

will = Student("William", 20, 100, 99)
print(f"Hey {will.name}, You have {will.calculate()} marks and grade {will.grade()}")


# Creating a product catalog
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate(self):
        return self.price * self.quantity

rice = Product("Rice", 110, 10)
print(f"The total value of {rice.name} is Kes.{rice.calculate()}")

milk = Product("Milk", 30, 60)
print(f"I will buy {milk.name} for my family. It will cost me Kes.{milk.calculate()}")



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # behaviours | methods
    def get_capitalised_name(self):
        return self.__convert_to_upper_case(self.name)
    # The __ are put to show it's used internally and should not be accessed externally
    
    def __convert_to_upper_case(self, name):
        return name.upper()
    
    def make_sound(self):
        pass

dog = Animal("Milo", 40)
print(dog.get_capitalised_name())