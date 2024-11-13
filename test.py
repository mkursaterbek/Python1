class BankAccount:
    def __init__(self, username, balance, id, amount):
        self.user = str(username)
        self.balance = float(balance)
        self.id = int(id)
        self.amount = float(amount)

    def withdraw(self):
        if self.amount < self.balance:
            self.balance -= self.amount
            print(f"Kalan bakiye: {self.balance}")
        else:
            print("Yetersiz bakiye!")

    def deposit(self):
        self.balance += self.amount
        print(f"Güncel bakiye: {self.balance}")

# Sınıf dışındaki fonksiyon
def deposit_money(ornek):
    amount = float(input("Ne kadar para yatırmak istiyorsunuz? : "))
    # Yatırılacak miktarı nesneye aktar ve deposit işlemi yap
    ornek.amount = amount
    ornek.deposit()

# Sınıfın bir örneğini oluşturuyoruz
ornek_nesne = BankAccount("arda", 700, 999, 8)

# Sınıf dışındaki fonksiyon ile para yatırma işlemi yapıyoruz
deposit_money(ornek_nesne)
