#5
print("KBTU BANK ?")
print()

class Account:

    owner = input("Your name: ")
    balance = 0

    def deposit(self,amount_of_money):
        Account.balance += amount_of_money
        print()
        print(f"{amount_of_money} was added to your balance.")
        print(f"Your current balance: {Account.balance}")

        print()

    def withdraw(self,amount_to_take):

        if amount_to_take <= Account.balance:
            print("Successfully !, good luck :D", f"{amount_to_take} was taken from your balance.")
            Account.balance -= amount_to_take
            print()
            print(f"Your current balance: {Account.balance}")
            print()
        else:
            print()
            print("Oops!, your current balance is less than you want to take !")
            print()
            print(f"Your current balance: {Account.balance}, but you want to take {amount_to_take}.")


kbtu = Account()

kbtu.deposit(5000)
kbtu.withdraw(2500)
kbtu.withdraw(5000)
print()
