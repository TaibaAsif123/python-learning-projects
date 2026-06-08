
"""
This program simulates a slot machine game where the user spins for matching symbols
to win payouts based on the symbol type and bet amount
"""

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("***********")
    print("|".join(row))
    print("***********")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100
    print("************************")
    print("WELCOME TO SLOTS MACHINE")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Invalid input, please enter a numeric bet.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds.")
            continue
        if bet <= 0:
            print("Bet must be positive.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning......")
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"YOU WON ${payout}!")
        else:
            print("You lost this round.")
        
        balance += payout
        play_again=input("do u want to play again?Y/N").upper()
        if play_again!='Y':
            break
    print("Game Over!")
    print(balance)
    

if __name__ == '__main__':
    main()
