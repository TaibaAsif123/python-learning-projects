
"""
This program simulates a vending machine that accepts coins (25, 10, 5 cents),
tracks the amount due, and calculates change owed once the total reaches 50 cents
"""
amount_due = 50

while amount_due > 0:
    coin = int(input("Insert Coin: "))

    # Accept only valid coin inputs
    if coin in [25, 10, 5]:
        amount_due -= coin
        if amount_due > 0:
            print("Amount Due:", amount_due)
        else:
            print("Change Owed:", abs(amount_due))
    else:
        print("Amount Due:", amount_due)
