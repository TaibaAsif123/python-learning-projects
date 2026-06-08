
# This program converts weight between kilograms and pounds based on user input

weight=float(input("Enter your weight:"))
choice=input("kg or pounds?")
if choice=="pounds":
    pounds=weight*2.2
    print(f"Your weight {weight}kg is {round(pounds,1)} pounds")
elif choice=="kg":
    kg=weight/2.2
    print(f"Your weight {weight}pounds is {round(kg,1)} kg") 

