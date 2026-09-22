'''
Polymorph :

Poly ==> many
morph ==> forms

Types of polymorphism:
1. compile-time
    1. Function overloading
    2. Operator overloading
2. Run-time
    1. Method overriding
'''
print(10 + 20)
print("abc" + "xyz")

#1. Function overloading
def add(x,y):
    return x + y 

def add(x,y,z):
    return x + y + z 

def add(x,y,z,a):
    return x + y + z + a 

#print(add(10,20))
#print(add(10,20,30))
print(add(10,20,30,40))
'''
Python does not support Function overloading directly
we can achieve this using variable length arguments'''

def add(*values):
    return sum(values)

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

#Operator overloading
class Add:
    def __init__(self,x):
        self.x = x
    def __add__(self,val):
        return self.x + val.x
    def __sub__(self,val):
        return self.x - val.x
    def __lt__(self,val):
        return self.x < val.x

a = Add(10)
b = Add(20)
print(a + b)
print(a - b)
print(a < b)

#Method overriding:
'''
same method in parent and chils class is known as Method overiding
'''
class Parent:
    def display(self):
        print("Parent class display method")

class Child(Parent):
    def display(self):
        print("Child class display method")

c = Child()
c.display() #child class method
Parent.display(c) #Parent class method