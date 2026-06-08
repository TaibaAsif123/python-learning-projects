
"""
This program looks up and displays calorie counts for various fruits based on 
user input, using a predefined dictionary of fruit-to-calorie mappings
"""

def main():
    # Dictionary mapping fruits to their calories
    items = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt user for input
    item = input("Item: ").strip().lower()

    # Check if the fruit is in the dictionary and print the calories
    if item in items:
        print(f"Calories: {items[item]}")
    else:
        pass  # Ignore input that isn't a fruit

if __name__ == "__main__":
    main()
