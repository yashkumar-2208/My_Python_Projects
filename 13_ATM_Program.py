import time
balance = 0

def show_balance():
    print(f"Your bank balance is: ₹{balance:.2f}")

def deposite_money():
    amount = float(input("Enter amount to be deposited: "))

    if amount <= 0:
        print("The amount should not be 0 or less than zero")
        return 0
    else:
        print(f"₹{amount:.2f} has deposited successfully!")
        return amount

def withdraw_money():
    amount = float(input("Enter amount to be withdrawn: "))


    if amount <= 0:
        print("Amount must be greater than 0")
        return 0

    elif amount > balance:
        print("Insufficient bank balance")
        return 0

    else:
        print(f"Withdrawing your amount wait for 2 seconds")
        time.sleep(2)
        print(f"₹{amount}Amount has been withdrawl!")
        return amount
        

is_running = True

while is_running:
    print("\n--- Banking Program ---")
    print("1. Show balance")
    print("2. Deposite money")
    print("3. Withdraw money")
    print("4. Exit/Quit")

    choice = input("Enter your choice from (1-4): ")

    if choice == "1":
        show_balance()

    elif choice == "2":
        balance += deposite_money()

    elif choice == "3":
        balance -= withdraw_money()

    elif choice == "4":
        is_running = False
        
    else:
        print("Invalid choice!")

print("Thank you have a nice day!")