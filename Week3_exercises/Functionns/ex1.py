"""
Number Guessing Game:
Write a function called guess_number() 
that generates a random number between 1 and 10, 
asks the user to guess the number, 
and provides feedback on whether the guess is too high, too low, or correct. 
The function should keep prompting the user until they guess the correct number.
"""
import random

def guess_number(): 
    chosen_no = random.randint(1,10)
    guess_no = 0
    while(guess_no != chosen_no):
        guess_no = int(input("Guess the number (1-10): "))
        if (guess_no > chosen_no):
            print("Retry. Your number is too high :(")
        elif (guess_no < chosen_no):
            print("Retry. Your number is too low :(")
        
    print("Correct! The chosen number is", guess_no)
    
if __name__ == "__main__":
    guess_number()