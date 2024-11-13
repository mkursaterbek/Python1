from function import *

print(f" Please Select One Of The Following Pptions")
print(f"--------------------------- ")
print(f"1. Check Balance ")
print(f"2. withdraw money ")
print(f"3. Deposite Money")
print(f"4. View Account Information")
print(f"5. Create New Account")
print(f"6. Quit")


class BankAccount:
    def __init__(self, username, balance, id, amount):
        self.user= str(username)
        self.balance = float(balance)
        self.id = int(id)
        self.amount = float(amount)

    def withdraw(self):
        if self.amount < self.balance:
            self.balance -= self.amount
            print(f"Kalan bakiye: {self.balance}")

    def deposit(self):
        self.balance += self.amount
        print(f"Güncel bakiye: {self.balance}")

    def view_balance(self):
        print(f"Güncel bakiye: {self.balance}")

ornek_nesne = BankAccount("arda", 12, 999, 8 )
view_balance(ornek_nesne)
