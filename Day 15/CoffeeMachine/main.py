MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def generate_report():
    for r in resources:
        if r == "water" or r == "milk":
            print(f'{r.title()}: {resources[r]}ml')
        elif r == "coffee":
            print(f'{r.title()}: {resources[r]}g')
        else:
            print(f'{r.title()}: ${resources[r]}')


def check_resources(drink):
    water_required = MENU[drink]["ingredients"]["water"]
    if water_required > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if drink != "espresso":
        milk_required = MENU[drink]["ingredients"]["milk"]
        if milk_required > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    coffee_required = MENU[drink]["ingredients"]["coffee"]
    if coffee_required > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def balance_resource(drink):
    water_required = MENU[drink]["ingredients"]["water"]
    current_water = resources["water"]
    new_water = current_water - water_required
    resources["water"] = new_water
    if drink != "espresso":
        milk_required = MENU[drink]["ingredients"]["milk"]
        current_milk = resources["milk"]
        new_milk = current_milk - milk_required
        resources["milk"] = new_milk
    coffee_required = MENU[drink]["ingredients"]["coffee"]
    current_coffee = resources["coffee"]
    new_coffee = current_coffee - coffee_required
    resources["coffee"] = new_coffee


def do_coins(drink):
    price = MENU[drink]["cost"]
    print("Please insert coins")
    coins = []
    q = int(input("how many quarters?"))
    coins.append(q * 0.25)
    d = int(input("how many dimes?"))
    coins.append(d * 0.10)
    n = int(input("how many nickles?"))
    coins.append(n * 0.05)
    p = int(input("how many pennies?"))
    coins.append(p * 0.01)
    if sum(coins) < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(sum(coins) - price, 2)
        print(f"Here is your ${change} in change")
        current_money = resources["money"]
        new_money = current_money + price
        resources["money"] = new_money
        return True


def make_drink(drink):
    if check_resources(drink):
        if do_coins(drink):
            print(f"Here is your {drink} ☕ Enjoy!")
            balance_resource(drink)


power = True
while power:
    choice = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        generate_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        make_drink(choice)
    else:
        print("Powering down!")
        print("Goodbye")
        power = False
