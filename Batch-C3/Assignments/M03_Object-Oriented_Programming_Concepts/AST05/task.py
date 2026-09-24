from abc import ABC, abstractmethod
class Payment(ABC):
    pass

class UPI(Payment):
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        pass

class Cash(Payment):
    def pay(self, amount):
        pass

if __name__ == '__main__':
    payment_type = input()
    amount = int(input())

    if payment_type == "UPI":
        payment = UPI()

    elif payment_type == "CreditCard":
        payment = CreditCard()

    else:
        payment = Cash()

    payment.pay(amount)
