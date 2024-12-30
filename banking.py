def create_acc(data):
        name=input("Enter Your Name")
        data={
            "name":name,
            "balance":0.0,
            "transaction":[]
            
            }
        print(f"Account for {name} has been create.")
        return data
def money_dep(data):
    amount = float(input("Enter Your Amount: "))
    if amount <= 0:
            print("Invalid! Amount should be positive.")
    else:
            data["balance"] += amount
            data["transaction"].append(f"Deposit: +{amount:.2f}")
            print(f"Deposited: {amount:.2f} successfully. Total Amount: {data['balance']:.2f}")
    return data
def money_withdraw(data):
        amount=float(input("Enter Your Amount:"))
        if amount <=0:
            print("Invalid!Amount Should Be Positive")
        if amount >data['balance']:
            print("Insufficient Funds")
        else:
            data["balance"]-=amount
            data["transaction"].append((f"Withdraw: -{amount:.2f}"))
            print(f"Withdraw:{amount:.2f} Sucessfully.Total Amount:{data['balance']:.2f}")
        return data
def check_balance(data):
        print(f"Current Balance:{data['balance']:.2f}")
        return data
def trans_statement(data):
        print(f"""Transaction
                  {data["transaction"]}
                   Cuurent Balance:{data["balance"]}"""
             )
        return data
data=create_acc({})
while True:
        print("""welcome to bank
                 1.Create Account
                 2.Money deposit
                 3.Money Withdraw
                 4.Check Balance
                 5.Transaction
                 6.Exit""")
        select=int(input("Press the number"))
    
        if select == 1:
            data =create_acc(data)
        elif select == 2:
            data =money_dep(data)
        elif select == 3:
            data=money_withdraw(data)
        elif select == 4:
            data=check_balance(data)
        elif select == 5:
            data=trans_statement(data)
        elif select==6:
            break
        else:
            print("Invalid!you should select any number form 1 to 6 ")
    
print("Thank You! For Using Bank")
