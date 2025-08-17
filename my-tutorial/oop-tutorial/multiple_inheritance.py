class Bird:
    def fly(self):
        pass

class Mammal:
    def run(self):
        pass

class Bat(Bird, Mammal):
    def fly(self):
        return "Flying..."
    
    def run(self):
        return "Running...."

bat_one = Bat()
print(bat_one.fly())
print(bat_one.run())