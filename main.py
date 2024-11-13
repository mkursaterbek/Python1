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
    def __init__(self, username, balance ):
        self.user = username
        self.balance = balance
        
    def save_to_json(self, filename):
        data = {
            'name': self.user,
            'balance': self.balance 
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    
    def deneme(self):
        print(f"{self.user} = {self.balance} ")
    
    def load_to_json (self , filename):
        data ={ 
            'name' : self.user,
            'balance' : self.balance
        }
        with open(filename, 'r') as f:
            data = json.load(f)
        return self(data['name'], data['balance'])


person1 = BankAccount("Ali", 1000)
person2 = BankAccount("arda",2250)
person1.withdraw(2)
person2.deposit(250)
person1.save_to_json("data.json") 
person2.save_to_json("data.json") 
person1.deneme()
person2.deneme()

"""        
        
i=0
while i<1:
    choice = int(input("what is your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        withdraw_money()
    elif choice == 3:
        deposit_money()
    elif choice == 4:
        view_acount()
    elif choice == 5:
        create_new_acount()
    elif choice == 6:
        i = 3
        print("done")
    else:
        print("choice different")
        break"""


