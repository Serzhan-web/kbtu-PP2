class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal unsuccessful.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
mybalance=int(input("mybalamce:"))
account = Account(owner="Bekzat", balance=mybalance)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
account.deposit(a)
account.withdraw(b)
account.withdraw(c) 