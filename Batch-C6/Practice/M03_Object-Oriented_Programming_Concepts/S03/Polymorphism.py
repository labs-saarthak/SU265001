'''
Polymorphism:
Poly ==> Many
Morph ==> Forms

Types of polymorphism:
1. Compile-time
    1. Function overloading - creating multiple functions with same name
    and different argument list
    2. Operator overloading
2. Run-time
    1. Method overriding
'''

print(10 + 20)
print("abc" + "xyz")

#Function overloading
def add(a,b):
    return a + b
def add(a,b,c):
    return a+b+c
def add(a,b,c,d):
    return a+b+c+d

'''
Python does not support FUnction overloading directly
we can achieve this using variable-length arguments(using *)'''
def add(*values):
    return sum(values)

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

#Operator overloading
class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,val):
        return self.x + val.x
    def __lt__(self,val):
        return self.x < val.x 
    def __sub__(self,val):
        return self.x - val.x

a = A(10)
b = A(20)
print(a + b)
print(a - b)
print(a < b)


#Example
class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,val):
        return (self.x+val.x,self.y+val.y)
    def __sub__(self,val):
        return (self.x-val.x,self.y-val.y)

a = B(10,20)
b = B(30,40)
print(a + b) #(40,60)
print(a - b) #(-20,-20)

#Method overriding : Same method in both parent and child class
class Parent:
    def display(self):
        print("Parent class display method")

class Child(Parent):
    def display(self):
        print("Child class display method")

c = Child()
c.display()#child class method
Parent.display(c)#parent class method

# Duck typing
class Dog:
    def Sounds(self):
        print("Bark")
class Cat:
    def Sounds(self):
        print("Meow")

def make_sound(animal):
    animal.Sounds()

make_sound(Dog())
make_sound(Cat())
