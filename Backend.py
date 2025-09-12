import time

print("------------ Bank Account ---------------")
print("Welcome to Simple Bank Simulator!")


balance = 0 
usernames = []
passwords = []
emails = []
phone_number = []

def register():
    email= input("Enter your email: ")
    emails.append(email)
    phone = input("Enter your phone number: ")
    phone_number.append(phone)
    new_username = input("Enter your username (With this you can sign up.): ")
    key = input("Enter your password: ")

    if new_username not in usernames:
        usernames.append(new_username)
        passwords.append(key)
        print("\nSuccesfully register!\n")
    else:
        print("This username is already used, please try with other diferent!")
    
    
    print(phone_number + emails + usernames + passwords)
    time.sleep(1)
    return main()

def signup():

    while True:

        u1 = input("Enter username: ")
        w1 = input("Enter Password: ")

        if u1 in usernames:
            idx = usernames.index(u1)
            if passwords[idx] == w1:
                print("\nLogin succesful!\n")
                time.sleep(1)
                menu()
                return
            else:
                print("\nIncorrect password, please try again!\n")
                time.sleep(1)
        else:
            print("\nUser not found, please try again or sign up!\n")
            time.sleep(1)
            return main()

def check_balance():
    print(f"\nYour current balance is ${balance}\n")
    time.sleep(1)
    return balance

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

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew ${amount}!")
        return balance

def menu():
    global balance

    while True:

        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout\n")

        user_input = input("Choose an action: ")

        if user_input == "1":
            balance = deposit(balance)
        elif user_input == "2":
            balance = withdraw(balance)
        elif user_input == "3":
            balance = check_balance()
        elif user_input == "4":
            print("Logging out...")
            time.sleep(1)
            
            return main()
        else:
            print("Incorrect option, please try again.")


def main():
    print("1. Sign Up\n2. Register\n0. Quit")
    user_input = input("Choose an option: ")
    if user_input == "1":
        return signup()

    elif user_input == "2":
        return register()
    
    elif user_input == "0":
        print("GoodBye!!!")
        exit()

    else:
        print("Invalid option, please try again!")
        return main()
main()
