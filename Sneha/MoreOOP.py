""" Bank-Transaction classes"""
import datetime
import uuid

# class BankAccount:
#     def __init__(self) -> None:
#         self.account_holder = "Elon Muškić"
#         self.balance = 100000 #lol for him, we can to float("inf")


class BankAccount:
    def __init__(self, account_holder:str, balance) -> None:
        self.account_holder = account_holder
        self.balance = balance #lol for him, we can to float("inf")
        self.transactions = []



#setter
    def deposit(self, amt:float, transaction):
        if amt > 0: 
            self.balance += amt
            self.transactions.append(transaction)
            print(f"{amt} deposited.")

    def withdraw(self, amt:float, transaction):
        if amt > 0:
            self.balance -= amt
            self.transactions.append(transaction)
            print(f"{amt} withdrawn.")

    def check_balance(self): 
        return self.balance 
    
    def account_info(self):
        print(f"Dear {self.account_holder}, you currently have {self.balance}.")




# elon: BankAccount = BankAccount()
# print(elon.balance) 
# elon.account_info()
# elon.deposit(10000)
# print(elon.check_balance())

# print(elon.balance > 10000000)

# elon.withdraw(1000000)
# print(elon.account_info()) #lol elon in debt 



class Transaction:
    def __init__(self, tType, tAMT:float) -> None:
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type =tType
        self.transaction_amount = tAMT
        self.transaction_date = datetime.datetime.now()

    def display_transactions(self):
        # Return the transaction details
        return (f"Transaction ID: {self.transaction_id}\n"
                f"Type: {self.transaction_type}\n"
                f"Amount: {self.transaction_amount}\n"
                f"Date: {self.transaction_date}\n")


account = BankAccount("Sneha Roy", 100000000)
transaction = Transaction("deposit", 500)

account.deposit(500, transaction)

account.account_info()


for t in account.transactions:
    print(t.display_transactions())