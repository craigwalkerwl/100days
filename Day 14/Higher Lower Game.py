import random
from art import logo, vs
from game_data import data
import os

def clear():
    """Clear the screen."""
    os.system('cls' if os.name=='nt' else 'clear')

def get_data(a):
    choice = random.choice(data)
    while choice == a:
        choice = random.choice(data)
    return(choice)

def compare(guess, other, score):
    if guess["follower_count"] > other["follower_count"]:
        return score + 1
    else:
        score = 0
        return score

game_over = False
score = 0
a = random.choice(data)
b = get_data(a)

while not game_over:
    clear()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
    print(vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        guess = a
        other = b
    else:
        guess = b
        other = a

    new_score = compare(guess, other, score)
    if new_score > score:
        a = b
        score = new_score
        b = get_data(a)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
