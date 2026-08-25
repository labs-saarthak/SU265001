'''
What is a Class?
A class is a blueprint/template for creating objects.
It defines:

Attributes → data/properties
Methods → behavior/functions

What is an Object?
An object is an instance of a class.

Types of variables:
1. class variable
2. local variable
'''


class Example:
    x = 100 #class variables
    def display(self):
        print("This is Example class display method")

obj = Example()
obj.display()
print(obj.x)

# class Circle with two methods - Area,Perimeter
from math import pi
class Circle:
    r = 7
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r 

c = Circle()
'''
print(c.Area())
print(c.Perimeter())
print(dir(Circle))
'''
class A:
    pass

print(dir(A))