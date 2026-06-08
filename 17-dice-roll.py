
"""
This program simulates rolling a six-sided dice and displays the result using
ASCII art representations for each possible dice face (1-6)
"""

import random

def roll_dice():
    # List of ASCII art representations for each dice face
    dice_faces = { #dictionary
        1: (
            "-------\n"
            "|     |\n"
            "|  *  |\n"
            "|     |\n"
            "-------"
        ), #value is a tuple
        2: (
            "-------\n"
            "| *   |\n"
            "|     |\n"
            "|   * |\n"
            "-------"
        ),
        3: (
            "-------\n"
            "| *   |\n"
            "|  *  |\n"
            "|   * |\n"
            "-------"
        ),
        4: (
            "-------\n"
            "| * * |\n"
            "|     |\n"
            "| * * |\n"
            "-------"
        ),
        5: (
            "-------\n"
            "| * * |\n"
            "|  *  |\n"
            "| * * |\n"
            "-------"
        ),
        6: (
            "-------\n"
            "| * * |\n"
            "| * * |\n"
            "| * * |\n"
            "-------"
        )
    }

    # Roll the dice (random number from 1 to 6)
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!\n")
    print(dice_faces[roll])

# Roll the dice and print the ASCII art
roll_dice()
