"""
    MRO is the method in which python searches for methods in classes
    during method calls, especially in cases of multiple inheritance (when a class inherits from more than once parent class)
    It helps Python determine which method to execute whn there are method name conflicts or ambiguity due to inheritance.

    Python uses the C3 Linearization algorithm to calculate the MRO.
    It follows the depth-first left-right search pattern to maintan the order of inheritance
    and resolve method conflicts effectively.
"""

class A:
    def greet(self):
        return "Hello from class A"
    
class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

obj_d = D()
print(obj_d.greet())

"""
    Let’s break it down:

    Class D inherits from classes B and C, which in turn inherit from class A.
    When we call obj_d.greet(), Python follows the MRO to determine which greet() method to execute.
    The MRO for class D in this case is D -> B -> C -> A, following the depth-first left-to-right search.
    Python finds the greet() method in class B first (left-most class in inheritance), so it executes the greet() method from class B.
"""