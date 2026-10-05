# Global variable
balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("Updated balance:", balance)
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Updated balance:", balance)
# Menu-driven program
while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            deposit(amount)
        else:
            print("Enter a valid amount.")
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0:
            withdraw(amount)
        else:
            print("Enter a valid amount.")
    elif choice == "3":
        print("Current balance:", balance)
    elif choice == "4":
        print("Thank you for using the bank.")
        break
    else:
        print("Invalid choice. Please try again.")
#output:
--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 2000
Amount deposited: 2000.0
Updated balance: 3000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter withdrawal amount: 1000
Amount withdrawn: 1000.0
Updated balance: 2000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current balance: 2000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Thank you for using the bank.
