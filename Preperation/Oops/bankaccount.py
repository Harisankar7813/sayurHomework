class Bank_account:
    def __init__(self,balance):
        self.balance=balance
    def deposited(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited amount {amount} New balance {self.balance}")
        else:
            print(f"Invalid amount.please,enter a positive amount")
    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f"With draw amount {amount} New balance {self.balance}")
            else:
                print(f"Insufficient balance.cannot withdraw")
        else:
            print(f"Invalid amount.please enter a positive amount")
account=Bank_account(1000)
account.deposited(2000)
account.withdraw(500)

        