#Data Types

#String
print("Hello"[4])

#Integer
print(123+345)
print (123_456_789 + 1)

#Float
3.141592
import math
print(math.pi)

#Boolean
True
False

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has "+new_num_char+" characters.")

float_pi = math.pi
print(type(float_pi))
print(float_pi)
int_pi = int(float_pi)
print(type(int_pi))
print (int_pi)


print(3 + 5) #addition
print(7 - 4) #subtraction
print(3 * 2) #multiplication
print(6 / 3) #division - output's as float
print(type(6/3)) #division - output's as float
print(2 ** 3) #exponential (to the power of)

#PEMDAS - BODMAS -- LEFT TO RIGHT
# Parenthesis - Brackets
# Exponential - Order (Powers)
# Multiplication
# Division
# Addition
# Subtraction

# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))
print(8 // 3) # Floor division (makes bottom int)

score = 0
score += 1
print(score)

#f-String
score = 0 #int
height = 1.8 #float
isWinning = True # Bool
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
