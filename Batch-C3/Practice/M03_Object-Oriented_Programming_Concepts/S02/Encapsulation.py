'''
Encapsulation : 
1. Binding data and methods together
2. Data hiding

Access specifiers:
1. Public(name)
2. Protected(_name)
3. Private(__name)
'''
class A:
    a = 10
    _b = 20
    __c = 30

obj = A()
print(obj.a)
print(obj._b)
print(obj._A__c) 

#Data hiding --> Accessing and updating private members from methods

class Sample:
    def __init__(self,amount):
        self.__amount = amount

    def credit(self,value):
        self.__amount += value

    def debit(self,value):
        self.__amount -= value

    def display(self):
        print(self.__amount)

obj = Sample(1000)
obj.display()
obj.credit(1500)
obj.display()
obj.debit(500)
obj.display()