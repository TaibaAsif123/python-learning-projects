
"""
This program is a number guessing game where the user tries to guess a randomly
generated number between 1 and 100, receiving hints and tracking guess count
"""

import random

# Define the correct range for random number generation
low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)

print("Welcome to the GAME")
is_running = True
guesses = 0

while is_running:
    guess = input("Enter a number between 1-100: ")
    
    # Check if the input is a digit
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low_num or guess > high_num:
            print("Out of range")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print("CORRECT!")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("INVALID input. Please enter a number.")
