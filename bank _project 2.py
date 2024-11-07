import os
class Bank_account:
    def __init__(self, account_holder) -> None:
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        if amount > 0:
            print(f"Deposited: NGN {amount:,.2f}")
        else:
            print("Deposited amount is Low(negative), please amount must be in a Positive denomination.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Thank you for Withdrewing: NGN {amount:,.2f}.")
        else:
            print("Insufficient Funds.")

    def check_balance(self):
        print(f"Your current balance is: NGN {self.balance:,.2f}.")
 
    def header():
        print("Welcome to Flesh Bank.")

    def refresh_screen():
        os.system("cls")

    def main(self):

        Bank_account.header()
        account_holder = input("Holder enter your user ID : ").lower()
        self.account_holder = account_holder
        Bank_account.refresh_screen()
        print(f"Hello, {account_holder.upper()}.")
        account = Bank_account(account_holder)

        account.check_balance()
          
        while True:

            action = input(f"{account_holder.upper()}, Do you want to withdraw or Deposit or 'exit' to quit:  ").lower()
            if action == 'withdraw':
                amount = float(input("Enter the amount to withdraw: NGN "))
                account.withdraw(amount)
                account.check_balance()
            elif action  == 'deposit':
                amount = float(input("Enter the amount to deposit: NGN "))
                account.deposit(amount)
                account.check_balance()
            elif action == 'exit':
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("invalid input, Please type 'withdraw', 'deposit' or 'quit' ")
                
        Bank_account.refresh_screen()
        continue_action = input("Do you want to continue banking? (Yes or No): ").lower()
        if continue_action != 'yes':
            print(f"{account_holder.upper()} Thank you for banking with us. Goodbye!")
            
        
    
    
bank_account = Bank_account("Account Holder")
bank_account.main()
