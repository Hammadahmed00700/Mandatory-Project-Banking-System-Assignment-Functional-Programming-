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
