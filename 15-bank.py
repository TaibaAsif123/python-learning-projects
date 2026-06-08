
"""
This program evaluates a user's greeting and outputs a dollar amount based on
whether it starts with "hello" ($0), starts with "h" ($20), or anything else ($100)
"""

# Step 1: Prompt the user for a greeting
greeting = input("Greeting: ")

# Step 2: Normalize the input
greeting = greeting.strip().lower()

# Step 3: Check the conditions
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

#can also use indexing[0],and substring in string function