
"""
This program runs a Rock-Paper-Scissors game where the user plays against the computer,
tracking scores and allowing multiple rounds until the user decides to quit
"""

import random

# Game options and initial scores
options = ("Rock", "Paper", "Scissors")
user_score = 0
comp_score = 0
running=True
# Game loop
while running:
    # Computer's choice
    comp = random.choice(options)
    # Get user input
    user = input("Enter a choice (Rock, Paper, Scissors): ")
    
    # Check if user input is valid
    if user not in options:
        print("Invalid choice. Please try again.")
        continue

    # Display choices
    print(f"Computer chose: {comp}")
    print(f"You chose: {user}")
    
    # Determine the winner
    if (comp == "Rock" and user == "Paper") or \
       (comp == "Paper" and user == "Scissors") or \
       (comp == "Scissors" and user == "Rock"):
        print("User Wins")
        user_score += 1
    elif comp == user:
        print("It's a TIE")
    else:
        print("Computer Wins")
        comp_score += 1

    # Display scores
    print(f"User Score: {user_score} | Computer Score: {comp_score}")
    
    # Check if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        running=False
        break
