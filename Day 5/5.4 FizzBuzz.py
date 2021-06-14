s = ""
for n in range(1, 101):
  if n % 3 == 0:
    s += "Fizz"
  if n % 5 == 0:
    s += "Buzz"
  if n % 7 == 0:
    s += "Fuzz"
  if n % 9 == 0:
    s += "Bizz"
  if s == "":
    s += str(n)
  print(s)
  s = ""