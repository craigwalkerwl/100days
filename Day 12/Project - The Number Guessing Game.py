#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo
import os

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def clear():
    """Clear the screen."""
    os.system('cls' if os.name=='nt' else 'clear')

def check_answer(guess, answer, lives):
    '''Compare guess against answer and print reply, returns lives'''
    if guess > answer:
        print("Too high.")
        return lives - 1
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    '''Set game difficulty, 5 lives for hard, 10 lives for easy'''
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_LIVES
    else:
        return HARD_LEVEL_LIVES

def game():
    '''Play NUMBERS'''
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    lives = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, answer, lives)
        if lives == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")

game()