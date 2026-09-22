''' Type Checking: To check the value of particular class or data type:
type()
'''
a = 10
b = 5.6
c = "Ram"
d = [1,2,3,4,5,4]
e = (1,2,3,4,5)
f = {1,2,3,5,6}
g = {"name": "Kalyani"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

'''
isinstance(): to check the value/object is belongs to particular class or datatype
Syntax:
isinstance(obj, type)

It gives us Boolean value(True or False)
'''
a = 10
b = 5.6
c = "Ram"
d = [1,2,3,4,5,4]
e = (1,2,3,4,5)
f = {1,2,3,5,6}
g = {"name": "Kalyani"}
print(isinstance(a, int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,tuple))
print(isinstance(f,set))
print(isinstance(g,dict))

#Chcking multiple Values:
x =  "Ram"
if isinstance(x, (int,float)):
    print("Given x is int or float")
else:
    print("Given x is a String")

#checking with classes:
class Animal:
    pass
class Dog(Animal):
    pass
class cat:
    pass
d = Dog()
c = cat()
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance(c,Dog))
print(isinstance(c,cat))

#Duck Typing: same method acts as as same behaviour , we can use it
class Dog:
    def sound(self):
        print("Bow - Bow")
class Cat:
    def sound(self):
        print("Meow-Meow")
def make_sound(animal):
    animal.sound()
d = Dog()
c = Cat()
make_sound(d)
make_sound(c)

#Example:
def process(data):
    if isinstance(data,int):
        return data * 2
    elif isinstance(data,str):
        return data.upper()
    elif isinstance(data,float):
        return data * 10.5
print(process(10))
print(process('kalyani'))
print(process(10.56))

#Interview Question:
class A:
    pass
class B(A):
    pass
obj = B()
print(type(obj) == B)       #True
print(type(obj) == A)       #

print(isinstance(obj, B))     #True
print(isinstance(obj, A))     #


