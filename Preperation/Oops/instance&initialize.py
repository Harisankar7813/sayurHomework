class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited amount {amount} and balance {self.balance}")
        else:
            print(f"Invalid amount.please enter poistive amount")
    def with_draw(self,amount):
        if amount>0:
            if self.balance>0:
                self.balance-=amount
                print(f"Withdraw {amount}.New balance {self.balance}")
            else:
                print(f"Insuffocient balance")
        else:
            print(f"amount is invalid")
amount=BankAccount(98293928329,2000)
amount.deposite(1000)
amount.with_draw(100)