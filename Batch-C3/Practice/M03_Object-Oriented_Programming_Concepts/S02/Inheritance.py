'''
Acquiring properties from parent to child 

Types of Inheritance:
1. single
2. multi-level
3. Multiple
4. Hierarchical
5. hybrid
'''
#Single inheritance
class A:
    def display1(self):
        print("Class A display method")
class B(A):
    def display2(self):
        print("Class B display method")
b = B()
b.display2()
b.display1()

#Multi-level inheritance
class A:
    def display1(self):
        print("Class A display method")
class B(A):
    def display2(self):
        print("Class B display method")
class C(B):
    def display3(self):
        print("Class C display method")

#Multiple Inheritance
class A:
    def display(self):
        print("Class A display method")
class B:
    def display(self):
        print("Class B display method")
class C(A,B):
    def display1(self):
        print("Class C display method")
c = C()
c.display()

# MRO - Method Resolution Order
#Hierarchical 
class A:
    def display1(self):
        print("Class A display method")
class B(A):
    def display2(self):
        print("Class B display method")
class C(A):
    def display3(self):
        print("Class C display method")