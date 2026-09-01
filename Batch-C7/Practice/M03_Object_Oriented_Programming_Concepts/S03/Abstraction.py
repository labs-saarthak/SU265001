'''
Abstraction : It hides the internal Implementation,shows only essential Functions to the user
Ex:

ATM 
 |
Card 
 |
LAnguage
 |
withdraw
  |
Enter amount
  |
PIN
 |
Draw
Internal Implementation :
1. Bank Details Hides
2. Communication with Bank Server

#Implement the Abstraction in Python:
abc --> It is a module,We can create  Abstract class 
ABC --> Abstract Base Class,we can create Abstract Methods
abstractmethod --> Decorator, nothhing can implement
'''
from abc import ABC as Kalyani,abstractmethod

class Vehicle(Kalyani):
    @abstractmethod
    def sound(self):
        print("Vehicle makes sound")
class Car(Vehicle):
    def sound(self):
        print("Car make sound")
class Bike(Vehicle):
    def sound(self):
        print("Bike makes sound")
c = Car()
d = Bike()
c.sound()
d.sound()

#Write a Python Code using Abstraction of Payment Process(UPI,Paytm)?
#Assign amount through UPI-->500 and throughPatym-->1000?

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass 
class UPI(Payment):
    def pay(self,amount):
        print("Transac ruppees",amount,"through UPI")
class Paytm(Payment):
    def pay(self,amount):
        print("Transac ruppees",amount,"through Paytm")
u = UPI()
p = Paytm()
u.pay(500)
p.pay(1000)















