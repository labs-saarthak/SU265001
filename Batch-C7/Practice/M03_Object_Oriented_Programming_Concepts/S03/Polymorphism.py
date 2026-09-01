'''
Polymorphism : 

Poly --> Many
Morphism --> Forms

Same Method name with different Behaviours
'''
class Animal:
    def sound(self):
        print("Animal makes sound")
class Cat:
    def sound(self):
        print("Cat makes sound")
class Dog:
    def sound(self):
        print("Dog makes sound")
c = Cat()
d = Dog()
c.sound()
d.sound()

'''
JAVA -->Polymorphism -->Method Overriding , Method Loading
Python --> Polymorphism --> Method Overriding , Duck Typing

'''
#Method Overriding:Same method name with different Action
class Animal:
    def sound(self):
        print("Animal makes sound")
class Cat:
    def sound(self):
        print("Cat makes sound")
class Dog:
    def sound(self):
        print("Dog makes sound")
c = Cat()
d = Dog()
c.sound()
d.sound()

a = [Cat(),Dog()]
for obj in a:
    obj.sound()

#Method Loading :Same method name with different Arguments
class Cal:
    def add(self,a,b,c):
        print(a+b+c)
obj1 = add(10,20)
obj2 = add(10,20,30)

#Duck Typing :If it is required to access the object's method then python allow you to use it,without its type

class Dog:
    def sound(self):
        print("Bow-Bow")
class Cat:
    def sound(self):
        print("Meow-Meow")
def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())

#Inheritance in Polymorphism :
class Vehicle:
    def horn(self):
        print("Vehicle gives sound")
class Car(Vehile):
    def horn(self):
        print("Car gives sound")
class Bike(Vehicle):
    def horn(self):
        print("Bike gives sound")
        super().horn()  #Access the parent class method
for obj in [Car(),Bike()]:
    obj.horn()
























