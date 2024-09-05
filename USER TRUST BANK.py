Accounts={ }

def creat_account():
    account_number = int(input("Enter account number: "))
    name = input("Enter account holder name: ")
    in_balance = float(input("Enter in balance: "))

    if account_number in Accounts:
        print("account number already exist hee hee!")
    else:
        Accounts[account_number]={
            'Name': name,
            'Balance':in_balance
        }
        #print(f"Account created for {name} with balance {in_balance}")
        print(f"Account created for {name} with balance {in_balance} USER TRUST BANK! ")
        print(Accounts)

def withdraw_blance():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))

    if account_number in Accounts:
        if Accounts[account_number]['Balance']>= amount:
            Accounts[account_number]['Balance']-=amount
            print(f"Withdrew {amount} new balance is {Accounts[account_number]['Balance']} USER TRUST BANK!")
            print(Accounts)
        else:
            print("Insufficient funds. USER TRUST BANK!")
    else:
        print("Account number is not exist USER TRUST BANK!")

def deposit_blance():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to Deposit : "))

    if account_number in Accounts:
        Accounts[account_number]['Balance']+=amount
        print(f"Deposit {amount} new balance is {Accounts[account_number]['Balance']} USER TRUST BANK!")
        print(Accounts)
    else:
        print("Account number is not exist USER TRUST BANK!")
def check_blance():
    account_number = int(input("Enter account number: "))
    if account_number in Accounts:
        print(f"Balance for account {account_number} is {Accounts[account_number]['Balance']} USER TRUST BANK!")
        print(Accounts)
    else:
        print("Account number is not exist USER TRUST BANK!")

def main():
    while True:
        print("\nUSER TRUST BANK! Bank Management System ")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("USER TRUST BANK! Enter your choice: "))

        if choice == 1:
            creat_account()
        elif choice == 2:
            deposit_blance()
        elif choice == 3:
            withdraw_blance()
        elif choice == 4:
            check_blance()
        elif choice == 5:
            print("Exiting the system. Goodbye! USER TRUST BANK!")
            break
        else:
            print("Invalid choice. Please try again. USER TRUST BANK!")

#if __name__ == "__main__":
main()