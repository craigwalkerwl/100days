print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

lr = input('You encounter a crossroads leading left or right, which way do you choose? Type "Left" or "Right". ').lower()
if lr[0] == "l":
  print("You walk left down a long and winding road. After many hours of walking you end up at a river with a ferry crossing, but the boat is not there.")
  sw = input("Do you wait for the ferry or try to swim accross? Swim or Wait? ").lower()
  if sw[0] == "w":
    print("The ferry arrives after a few moments of waiting. You hop aboard to be faced with 3 doors. A red door, a yellow door and a blue door.")
    ryb = input("I guess you have to choose a door! Which door do you choose? Red, Yellow or Blue? ").lower()
    if ryb[0] == "y":
      print("You open the yellow door to find the ferry conrtol room, you navigate accross the river and disembark to discover a treasure chest.\nThe treasure chest contains a scrrol which reads:")
      print("The treasure is the journey and the friends you form along the way! WHAT A COP OUT!!  Game Over!")
    elif ryb[0] == "r":
      print("You open red door which is the engine furnace room, the door locks behind you and you burn to death in there. Game Over!")
    elif ryb[0] == "b":
      print("You open the blue door which leads to the lower deck, you follow it down and hear low beastly noises coming closer and closer.\nYou get eaten by the beasts of the lower deck. Game Over!")
    else:
      print("You didn't follow the rules and you get smited by the narrator. Game Over!")
  else:
    print("You attempt to swim accross the river, half way accross the river you get attacked and killed by trout. Game Over!")
else:
  print("You fall into a hole and die. Game Over!")