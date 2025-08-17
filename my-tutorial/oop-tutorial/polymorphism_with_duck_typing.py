class Dog:
    def make_sound(self):
        return "Woof"

class Cat:
    def make_sound(self):
        return "Meow"
    
class Bird:
    def make_sound(self):
        return "Crrckicki"


objects_list = []
bird_obj = Bird()
objects_list.append(bird_obj)
cat_obj = Cat()
objects_list.append(cat_obj)
dog_obj = Dog()
objects_list.append(dog_obj)

def let_them_speak(objs):
    return [obj.make_sound() for obj in objs]

print(let_them_speak(objects_list))

