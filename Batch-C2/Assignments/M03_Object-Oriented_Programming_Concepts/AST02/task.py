#Task
class BankAccount:
   def __init__(self, balance):
      pass

   def deposit(self, amount):
      pass

   def withdraw(self, amount):
      pass

   def get_balance(self):
      pass

if __name__ == '__main__':
   balance = int(input())
   deposit_amount = int(input())
   withdraw_amount = int(input())

   account = BankAccount(balance)

   account.deposit(deposit_amount)

   if not account.withdraw(withdraw_amount):
      print("Insufficient Balance")

   print("Balance:", account.get_balance())
