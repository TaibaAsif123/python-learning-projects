"""
This program implements a simple banking system where users can deposit money,
withdraw money, and check their balance with input validation and global variable management
"""

balance = 0

def show_balance():
    print(f"Your balance is {balance}")

def deposit(amount):
    global balance
    if amount<0:
        print("amount must be positive")
    else:
         balance += amount
         print(f"Your balance after deposit: {balance}")

def withdraw(amount):
    global balance
    if amount<balance:
        print("Insufficient balance")
    elif amount>0:
        print("Enter positive amount")
    else:
        balance -= amount
        print(f"Your balance after withdrawal: {balance}")

def main():
    is_running = True
    while is_running:
        choice = int(input("Do you want to DEPOSIT(1), WITHDRAW(2), or SHOW BALANCE(3)? Enter any other number to exit: "))
        match choice:
            case 1:
                a = int(input("Enter amount to deposit: "))
                deposit(a)
            case 2:
                a = int(input("Enter amount to withdraw: "))
                withdraw(a)
            case 3:
                show_balance()
            case _:
                print("Invalid input. Exiting.")
                is_running = False

if __name__ == '__main__':
    main()
