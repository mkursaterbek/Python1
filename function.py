import json
import random

def load_info():
    with open("./data.json") as f:
        return json.load(f)

def save_info():
    with open("./data.json", "wt", encoding="utf-8") as file:
        json.dump(arda, file, ensure_ascii=False, indent=4)

def random_id_number():
       return str(random.randint(1, 99999999))

def deposit_money(ornekdeposit):
    customer_deposite_amount= float(input(" how much money dou you want to deposite? : "))
    ornekdeposit.amount= customer_deposite_amount
    ornekdeposit.deposit()

def withdraw_money(ornekwithdraw):
     customer_withdraw_amount = float(input(" how much money dou you want to withdraw? : "))
     ornekwithdraw.amount = customer_withdraw_amount
     ornekwithdraw.withdraw()

def view_balance (ornekbalance):
     print(ornekbalance.balance)