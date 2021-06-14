import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if player_choice > 2 or player_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  computer_choice = random.randint(0, 2)
  rps = [rock, paper, scissors]
  print(rps[player_choice])
  print("Computer chose:")
  print(rps[computer_choice])
  if player_choice == computer_choice:
    print("DRAW!")
  elif rps[player_choice - 1] == rps[computer_choice]:
    print("You Win!")
  else:
    print("You Lose!")
