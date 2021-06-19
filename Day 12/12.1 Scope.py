################### Scope ####################
# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     potion_strength = 2 # LOCAL
#     print(potion_strength)

# drink_potion()
# print(potion_strength) # unavailable because potion_strength only exists in function

# Global Scope
# player_health = 10 # GLOBAL

# def drink_potion():
#     potion_strength = 2
#     print(player_health) #global can be used

# drink_potion()

# There is no Block Scope
# if 3 > 2:
#     a_variable = 10 # this will work anywhere, no fencing

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# Modifying Global Scope
enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Contants - use them as uppercase to show they're not to be changed
PI = 3.141592
URL = "https://www.google.com"