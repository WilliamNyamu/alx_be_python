# bank_account.py

class BankAccount:
    def __init__ (self, initial_balance = 0):
        self.__account_balance = initial_balance # Encapsulate the account_balance for protection and enforcing rules
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        return False # The pythonic way. Use this instead of nesting it with 'else'

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance}")
