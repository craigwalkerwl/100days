#Function
def greet():
    print(f"Hello")
    print(f"How do you do?")
    print("Isn't the weather nice today!")

greet()

#Function with 1 input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Craig")
greet_with_name("Dave")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Craig","Liverpool")

def my_function(a,b,c):
    print(a)
    print(b)
    print(c)

my_function("A", "B", "C")

greet_with(location="Liverpool",name="Craig")