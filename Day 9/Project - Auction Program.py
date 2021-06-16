import os
from art import logo

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

print(logo)
print("Welcome to the secret auction program.")

bid_dictionary = {}

auction_running = True
while auction_running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dictionary[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question == "no":
        auction_running = False
    else:
        clear()

b = 0
w = ""
for i in bid_dictionary:
    if bid_dictionary[i] > b:
        b = bid_dictionary[i]
        w = i

print(f'The winner is {w} with a bid of ${b}')