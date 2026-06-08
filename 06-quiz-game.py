
"""
This program is a simple quiz game that asks the user questions,
checks answers against a predefined list, and tracks the score
"""

questions=("what is 1+1:",
            "What is 2+2:")
options=(("A.2","B.5"),("8","B.4"))
answers=("2","4")
guesses=[]
score=0
question_num=0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter Guess:")
    guesses.append(guess)
    if guess==answers[question_num]:
        print("CORRECT!")
        score+=1
    else:
        print("INCOREECT!")
        print(f"Correct answer is:{answers[question_num]}")
    question_num+=1
