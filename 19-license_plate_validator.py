
"""
This program validates vanity license plates according to DMV rules: plates must be
2-6 characters, start with two letters, end with numbers (no letters after numbers),
first number cannot be zero, and no special characters allowed
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to validate vanity plate
def is_valid(s):
    # Check if the plate has between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check if numbers, if present, are only at the end and do not start with 0
    number_started = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            if not number_started:  # First number check
                if s[i] == '0':  # Numbers can't start with '0'
                    return False
                number_started = True
        elif number_started:
            return False  # No letters allowed after the numbers start

    # No periods, spaces, or punctuation marks allowed
    if not s.isalnum():  # Ensures all characters are alphanumeric (no special characters)
        return False

    # If all checks pass, the plate is valid
    return True

if __name__ == "__main__":
    main()
