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
}

user_inputs = [
    "espresso",
    "latte",
    "cappuccino",
    "report",
    "off"
]


def calculating_coins():
    """Function that receive how many coins of each and return its sum value"""
    coins = [
        float(input("How many quarters?: ")) * 0.25,
        float(input("How many dimes?: ")) * 0.10,
        float(input("How many nickels?: ")) * 0.05,
        float(input("How many pennies?: ")) * 0.01
    ]
    return sum(coins)


def check_resources(drink):
    """Function to check if there are enough resources to make the drink"""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_earned}")


# Creating money variable
money_earned = 0
purchase_try = 0
refund = 0
keep_going = True

print(resources)

# Getting the user Input
while keep_going:
    user = input("What would you like? ").lower()
    while user not in user_inputs:
        user = input("Choose a valid input: ")

    if user in ["latte", "espresso", "cappuccino"]:
        check = check_resources(user)
        if check:
            print("Please insert coins.")
            purchase_try = calculating_coins()
            if purchase_try - MENU[user]["cost"] < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money_earned += MENU[user]["cost"]
                if purchase_try > MENU[user]["cost"]:
                    refund = round(purchase_try - MENU[user]["cost"], 2)
                    print(f"Here is ${refund} dollars in change.")
                for ingredients, amounts in MENU[user]["ingredients"].items():
                    resources[ingredients] -= amounts
                print(f"Here is your {user}. Enjoy!")

    if user == "report":
        report()

    if user == "off":
        keep_going = False
