#author=Hammad ahmed
import os # for access form the system.
#step1 created function for  create account for user
def create_acc(data):
    if data:
        print("Account already exists.")
        return data
    name = input("Enter Your Name: ")
    data = {
        "name": name,
        "balance": 0.0,
        "transaction": []
    }
    print(f"Account for {name} has been created.")
    return data
#step2 created function for money depsoited 
def money_dep(data):
    amount = float(input("Enter Your Amount: "))
    if amount <= 0:
        print("Invalid! Amount should be positive.")
    else:
        data["balance"] += amount
        record_transaction(data, f"Deposit: +{amount}")
        print(f"Deposited: {amount:.2f} successfully. Remaining Amount: {data['balance']:.2f}")
    return data
#step3 created function for money withdrawal 
def money_withdraw(data):
    amount = float(input("Enter Your Amount: "))
    if amount <= 0:
        print("Invalid! Amount Should Be Positive.")
    elif amount > data['balance']:
        print("Insufficient Funds.")
    else:
        data["balance"] -= amount
        record_transaction(data, f"Withdrawal: -{amount}")
        print(f"Withdrawn: {amount:.2f} successfully. Remaining Amount: {data['balance']:.2f}")
    return data
#step2 created function for money check 
def check_balance(data):
    print(f"Current Balance: {data['balance']:.2f}")
#step5 created transaction history function
def trans_statement(data):
    print("\nTransaction Statement:")
    if not data["transaction"]:
        print("No transactions found.")
    else:
        for transaction in data["transaction"]:
            print(transaction)
    print(f"Remaining balance: {data['balance']:.2f}")

def record_transaction(data, transaction):
    data["transaction"].append(transaction)
    with open(f"{data['name']}_transactions.txt", "a") as file:
        file.write(transaction + "\n")

def load_transactions(data):
    filename = f"{data['name']}_transactions.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data["transaction"] = file.read().splitlines()
    return data

data = create_acc({})
data = load_transactions(data)

while True:
    #menu for user
    print("""
    Welcome to Bank:
    1. Create Account
    2. Money Deposit
    3. Money Withdraw
    4. Check Balance
    5. Transaction Statement
    6. Exit
    """)
    
    try:
        #user to select option
        select = int(input("Press the number: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")#handle error
        continue
    # Handle user selection
    if select == 1:
        data = create_acc(data)
    elif select == 2:
        money_dep(data)
    elif select == 3:
        money_withdraw(data)
    elif select == 4:
        check_balance(data)
    elif select == 5:
        trans_statement(data)
    elif select == 6:
        print("Thank You! For Using Bank.")# Exit the program
        break
    else:
        # Handle invalid menu options
        print("Invalid! You should select a number from 1 to 6.")
