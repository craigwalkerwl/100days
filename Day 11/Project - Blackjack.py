############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
    clear()
    print(logo)

    new_game = True
    while new_game:
        player_hand = []
        computer_hand = []
        player_hand.append(deal_card())
        player_hand.append(deal_card())
        print(player_hand)
        computer_hand.append(deal_card())
        print(computer_hand)
        # computer_hand = deal(hand=computer_hand, cards=1)
        new_game = False
    # print(f"Your cards: [{pcard1}, {pcard2}], current score: {pscaore}")
    # print(f"Computer's first card: {ccard1}")
    # another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    # if another_card == "y":
    #     draw_card(player)
    # else:
    #     draw_card(computer)
