# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_join = name1+name2
lower_name_join = name_join.lower()

t_count = lower_name_join.count("t")
r_count = lower_name_join.count("r")
u_count = lower_name_join.count("u")
e_count = lower_name_join.count("e")
true_score = t_count+r_count+u_count+e_count

l_count = lower_name_join.count("l")
o_count = lower_name_join.count("o")
v_count = lower_name_join.count("v")
love_score = l_count+o_count+v_count+e_count

final_score = int(str(true_score)+str(love_score))

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
