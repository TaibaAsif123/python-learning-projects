
# This program removes all vowels (both uppercase and lowercase) from a user-input string and displays the result

def remove_vowels(text):
    result = ""
    for vowel in text:
        if vowel not in ['a','e','i','o','u','A','E','I','O','I']:
            result += vowel
    return result

def main():
    user_input = input("Enter a string of text: ")
    no_vowels_text = remove_vowels(user_input)
    print("Text without vowels:", no_vowels_text)

if __name__ == "__main__":
    main()