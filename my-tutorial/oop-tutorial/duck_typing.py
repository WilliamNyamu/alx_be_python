"""
    Python uses a concept called "duck typing" to achieve polymorphic behavior.
    Duck typing emphasizes the object's behavior over its type or class. It's based on the idea
    that "if it looks like a duck and quacks like a duck, then it must be a duck"
"""

class Duck:
    def quack(self):
        return "Duck quacks"
    
class Person:
    def quack(self):
        return "Person imitates duck"

# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()

duck_obj = Duck()
person_obj = Person()

print(make_sound(duck_obj))
print(make_sound(person_obj))