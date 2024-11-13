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

arda= load_info()


def deposit_money():
    user_id = str(input("whats your id :"))
    if user_id in arda:
        deposite_money_amount= float(input("how much money dou you want tu deposite? "))
        old_balance= float(arda[user_id]["balance"])
        arda[user_id]["balance"]  = str(old_balance + deposite_money_amount)
        save_info()
    else:
        print("fuck of")

def withdraw_money():
    user_id = str(input("whats your id :"))
    if user_id in arda:
        withdraw_money_amount= float(input("how much money dou you want tu withdraw? "))
        old_balance= float(arda[user_id]["balance"])
        arda[user_id]["balance"]  = str(old_balance - withdraw_money_amount)
        save_info()
    else:
        print("fuck of")

def check_balance():
    user_id = str(input("whats your id :"))
    if user_id in arda:
        print(arda[user_id]["balance"])
    else:
        print("User ID not found.")
    
def view_acount():
    user_id = str(input("whats your id :"))
    if user_id in arda:
        print(arda[user_id])

def create_new_acount():
    random_id = random_id_number()
    name= input("what is your name? ")
    surname= input("what is your surname? ")
    date_of_birth= input("write your date of birth")
    mother_surname= input("What was your mother's surname before marriage? ")
    phone= input("What is your phone number?")
    mail= input("what is your e_mail? ")
    job= input("what is your job?")
    salary= input("what is your salary? ")
    transactions= input("how many transactions per month? ")
    balance = input("how much money do you want to deposite")
    arda[random_id] = {
        "name": name,
        "surname": surname,
        "date_of_birth": date_of_birth,
        "mother_surname": mother_surname,
        "phone": phone,
        "mail": mail,
        "job": job,
        "salary": salary,
        "transactions": transactions,
        "balance": balance
    }
    save_info()
            
