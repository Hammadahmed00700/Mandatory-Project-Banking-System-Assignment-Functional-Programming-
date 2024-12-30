def create_acc(data):
        name=input("Enter Your Name")
        data={
            "name":name,
            "balance":0.0,
            "transaction":[]
            
            }
        print(f"Account for {name} has been create.")
        return data
