# Menu of Coffee Machine
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

# Resources of Coffee Machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# All Possible Inputs from the User
user_inputs = [
    "espresso",
    "latte",
    "cappuccino",
    "report",
    "off"
]


def calculating_coins():
    """Function that receives how many coins the user has of each type, converts to dollar, and returns the total"""
    while True:
        try:
            coins = [
                int(input("How many quarters?: ")) * 0.25,
                int(input("How many dimes?: ")) * 0.10,
                int(input("How many nickels?: ")) * 0.05,
                int(input("How many pennies?: ")) * 0.01
            ]
            return sum(coins)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def check_resources(drink):
    """Function to check if there are enough resources to make the drink, returns boolean"""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def report():
    """Function that prints out the resources left in the coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_earned}")


def get_user_input():
    """Function to get a valid user input from the list user_inputs[]"""
    while True:
        input_user = input("What would you like? ").lower()
        if input_user in user_inputs:
            return input_user
        print("Choose a valid input: ")


def make_coffee(drink):
    """Function to make a coffee"""
    global money_earned
    check = check_resources(drink)
    if check:
        print("Please insert coins.")
        purchase_try = calculating_coins()
        if purchase_try - MENU[drink]["cost"] < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money_earned += MENU[drink]["cost"]
            if purchase_try > MENU[drink]["cost"]:
                refund = round(purchase_try - MENU[drink]["cost"], 2)
                print(f"Here is ${refund} dollars in change.")
            for ingredients, amounts in MENU[drink]["ingredients"].items():
                resources[ingredients] -= amounts
            print(f"Here is your {drink}. Enjoy!")


# All actions that should happen according to user_input
actions = {
    "latte": lambda drink: make_coffee(drink),
    "espresso": lambda drink: make_coffee(drink),
    "cappuccino": lambda drink: make_coffee(drink),
    "report": lambda _: report(),  # Ignore the argument
    "off": lambda _: exit()  # Ignore the argument
}

# Creating money variable
money_earned = 0

print(resources)

# Getting the user Input
while True:
    user = get_user_input()
    action = actions.get(user)
    if action:
        action(user)
