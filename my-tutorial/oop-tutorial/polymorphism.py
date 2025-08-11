from abc import ABC, abstractmethod

class Animal(ABC):
    name: str

    @abstractmethod
    def speak(self) -> str:
        pass
    # Pass because all the implementation will be handled by the class inheriting  it

class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def speak(self) -> str:
        return "Wooff!!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!!!"

animals = []
cat_names = ['milo', 'tom']
dog_names = ['sport', 'bosco']

for cat_name in cat_names:
    animals.append(Cat(cat_name))

for dog_name in dog_names:
    animals.append(Dog(dog_name))

def print_animal_name_and_sound(animals: list[Animal]):
    for animal in animals:
        print(f"name: {animal.name} | speak: {animal.speak}")
    pass

print_animal_name_and_sound(animals)