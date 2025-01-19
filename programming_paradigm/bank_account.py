
class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = float(account_balance)
    
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return  False
    def display_balance(self):

        print(f"Current Balance:  ${self.balance}")
    
    
