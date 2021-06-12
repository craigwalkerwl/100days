# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = weight / height ** 2
if bmi < 18.5:
  print(f"Your BMI is {bmi:.2f} which classifies you as underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi:.2f} which classifies you as normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi:.2f} which classifies you as overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi:.2f} which classifies you as obese")
else:
  print(f"Your BMI is {bmi:.2f} which classifies you as clinically obese")


