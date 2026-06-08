
"""
This program implements a Hangman word guessing game where the player tries to guess
letters in a randomly selected word, with hangman graphics displayed for wrong guesses
"""

import random
words=("apple","orange","banana","coconut","pineapple")
hangman_art={0:("   ",
                "   ",
                "   "),
             1:(" O ",
                "   ",
                "   "),
             2:(" O ",
                " | ",
                "   "),
             3:(" O ",
                "\| ",
                "   "),
             4:(" O ",
                "\|/",
                "   "),
             5:(" O ",
                "\|/",
                "/  "),
             6:(" O ",
                "\|/",
                "/ \ "),
}

#whenever there is wrong guess
def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
       print(line)
       

def display_hint(hint):
    print(" ".join(hint))
#when u lose or win
def display_answer(answer):
   print(" ".join(answer))
    
def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    is_running=True
    guessed_letter=set()
    while is_running:
     display_hangman(wrong_guesses)
     display_hint(hint)
     guess=input("Enter a Guess:").lower()
     #INPUT VALIDATION:
     if len(guess)!=1 or guess.isalpha():
        print("INVALID")
        continue
     if guess in guessed_letter:
        print("ALREADY GUESSED")
        continue
     #if guess is not made append it to your set
     guessed_letter.add(guess)
     #if correct guess:
    if guess in answer:
        for i in range(len(answer)):
           if answer[i]==guess:
              hint[i]=guess
           else:
              wrong_guesses+=1
    #if all underscores were fills means u win:          
    if "_" not in hint:
       display_hangman(wrong_guesses)   
       display_answer(answer)
       print("You Win")
       is_running=False  
    elif wrong_guesses>len(hangman_art)-1:
       display_hangman(wrong_guesses)
       display_answer(answer)
       print("You Lose")
       is_running=False
           



if __name__== '__main__':
    main()