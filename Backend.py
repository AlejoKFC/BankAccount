import time

print("------------ Bank Account ---------------")
print("Welcome to Simple Bank Simulator!\nYour Balance is: $0.00\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")

balance = 0 

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print (f"Deposited ${amount}!")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew ${amount}!")
        return balance


def check_balance(balance):
    print(f"Your current balance is {balance}")

def menu():
    global balance

    while True:
        user_input = input("Choose an action: ")

        if user_input == "1":
            balance = deposit(balance)
        elif user_input == "2":
            balance = withdraw(balance)
        elif user_input == "3":
            balance = check_balance(balance)
        elif user_input == "4":
            print("Thanks for using the Bank Simulator!")
            time.sleep(2)
            print("Exiting...\n---------------------------------------")
            break
        else:
            print("Incorrect option, please try again.")

menu()