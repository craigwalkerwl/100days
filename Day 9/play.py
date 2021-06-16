programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Loop"])

#Adding new items to Dictionary.
programming_dictionary["Four"] = "Something about 4."
print(programming_dictionary)
print(programming_dictionary["Four"])

#Create an empty Dictionary.
empty_dictionary = {}
print(empty_dictionary)

#Wipe an existing Dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a Dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

#Loop through in a Dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting list in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log)
print(travel_log["France"])
print(travel_log["France"][0])

#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3},
}

print(travel_log)
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["France"]["cities_visited"][0])
print(travel_log["France"]["total_visits"])

#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 3,
    },
]
print(travel_log)
print(travel_log[0])
print(travel_log[0]["country"])
print(travel_log[0]["cities_visited"])
print(travel_log[0]["cities_visited"][0])
print(travel_log[1]["total_visits"])
