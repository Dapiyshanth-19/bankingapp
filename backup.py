import os
import random

#user information==========================================
accounts={}
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
        


def create_account():
    account_number= random.randint(1000000000, 9999999999)
    if account_number in accounts:

        print("account number is alredy exists!.try again.")
    
        return
    name=input("enter the user name:")
    initial_balance=float(input("enter the intial balnace."))

    accounts[account_number] ={"name" :name,"balance": initial_balance}
    print(f"account created successfully! account number :{account_number}")

def view_all_customers():
    try :
        with open("customer.txt", "r") as customer_file:
            customers = customer_file.readlines()
            if  customers:
        
                for costomer in customers:
                    print(customer.strip())
            else:
                print("nocustomer records found!")
    except :
        print("no customer  records found!")

print("Press:\n 1. To create a customer\n 2. To view all customers")
get_input = int(input("enter the number: "))

if get_input == 1:
    create_customer_and_users()
elif get_input == 2:
    view_all_customers() 
else:
    print("invalid input. please enter number 1 or 2")

"""

def deposit_money():
    






#creat_account_number


account_number=print(account_number)


#=======================


print("=====MENU=====")
print("1.creat a account")
print("2.deposit money")
print("3.withdraw money")
print("4.check balance")
print("5.transaction history")
print("6.exit.")

choice=input("choose 1-4 option")
    if choice=="1":
        creat_account()
        elif choice=="2":
            deposit_money()
        elif choice=="3"
            withdraw_money()
        elif choice=="4"
            check_balance()
        elif choice=="5"
            transaction_history()
        elif choice=="6"
            print("exiting programe. thank you for using our service!")
            break
        else:
            print("invalid option. try again!")    


    
main()
"""