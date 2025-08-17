class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

rectangle_one = Rectangle(3, 5)
print(rectangle_one.calculate_area())