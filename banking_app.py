import os
import random

CUSTOMER_FILE = "customer.txt"

#======================================================================================================
accounts={}

def load_customers():
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                account_number, name, balance = parts[0], parts[1], float(parts[2])
                transactions = parts[3:]
                accounts[account_number] = {"name": name, "balance": balance, "transactions": transactions}

def save_customers():
    with open(CUSTOMER_FILE, "w") as file:
        for account_number, data in accounts.items():
            file.write(f"{account_number},{data['name']},{data['balance']},{','.join(data['transactions'])}\n")
def create_account():
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if account_number not in accounts:
            break  

    name = input("enter the user name: ")
    initial_balance = float(input("enter the initial balance: "))

    if initial_balance<0:
        print("initial balance must be non-negative.")
        return

    accounts[account_number]={"name": name, "balance": initial_balance, "transactions": []}
    save_customers() 
    print(f"account created successfully.account number:{account_number}")

def get_customer_info():
    user_name = input("enter the name :")
    if user_name.isalpha():
        print("valid name")
    else:
        print("your input contains non-alphabetical characters.")
    address =input("enter the customer address :")
    NIC_number =input("enter the NIC number:")
    password =input("enter the password :")
    return[user_name,address,NIC_number,password]
#account creation=========================================================
def create_customer_next_id():
    try: 
        with open("customer.txt","r")as customer_file:
            lines = customer_file.readlines()
            if lines:
                last_id = int(lines[-1].split(",")[0][1:])
                return f"u{last_id + 1:03}"
            else: 
                return "u001"
    except:
        return"uoo1"
print(create_customer_next_id())
            
       
    
def create_customer_and_users():
    with open("customer.txt", "a")as customer_file:
        customer_info = get_customer_info()
        customer_id = create_customer_next_id()
        customer_file.write(f"{customer_id},{','.join(customer_info)}\n")
        print("Customer added successfully!")
#deposit money==================================================================
def deposit_money():
    print("deposit money into an existing account")
    
    account_number = input("enter account number: ")
    
    if account_number not in accounts:
        print("account not found!")
        return

    amount = float(input("enter amount to deposit: "))
    
    if amount <= 0:
        print("deposit amount must be positive!")
        return

    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append(f"Deposited: {amount}")
    print("deposit successful!")

#withdraw money==================================================================
def withdraw_money():
    print("withdraw money from an existing account")
    account_number = input("Enter account number: ")
    
    if account_number not in accounts:
        print("account not found!")
        return

    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("withdrawal amount must be positive.")
        return
    
    if amount>accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return
    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append(f"Withdrew: {amount}") 
    print("withdrawal successful!")

#check balance======================================================================
def check_balance():
    print("check the current balance of an account")
    account_number = input("enter account number: ")

    if account_number not in accounts:
        print("account not found!")
        return

    print(f"Current balance: {accounts[account_number]['balance']}")
#transaction history========================================================================= 
def transaction_history():
    print("view all past transactions in the account")
    account_number = input("Enter  the account number: ")
    
    if account_number not in accounts:
        print("account not found! enter the correct account number.")
        return

    print("transaction history:")
    for transaction in accounts[account_number]["transactions"]:
        print(transaction)
def view_all_customers():
    try :
        with open("customer.txt", "r") as customer_file:
            customers = customer_file.readlines()
            if  customers:
        
                for costomer in customers:
                    print(customer.strip())
            else:
                print("no customer records found!")
    except :
        print("no customer records found!")

def main():
    while True:
        print("\n====MENU====")
        print("1.create a account")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.check balance")
        print("5.transaction history")
        print("6.exit.")

        choice=input("choose 1-6 option :")
        if choice=="1":
            create_account()
        elif choice=="2":
            deposit_money()
        elif choice=="3":
            withdraw_money()
        elif choice=="4":
            check_balance()
        elif choice=="5":
            transaction_history()
        elif choice=="6":
            print("exiting programe. thank you for using our service!")
            break
        else:
            print("invalid option. try again!")    



print("Press:\n 1. To create a customer\n 2. To view all customers")
get_input = int(input("enter the number: "))

if get_input == 1:
    create_customer_and_users()
elif get_input == 2:
    view_all_customers() 
else:
    print("invalid input. please enter number 1 or 2")


main()


