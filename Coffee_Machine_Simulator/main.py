# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO 3. Print report.
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

power_on = True
profit = 0.00


def process_drink():
    """Function used to process the drink selected by the user and reduce the resources correspondingly."""
    resources["water"] = resources["water"] - MENU[f"{answer}"]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[f"{answer}"]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[f"{answer}"]["ingredients"]["coffee"]


while power_on:
    answer = input("What would you like to drink? (espresso ($1.50) / latte ($2.50) / cappuccino $3.00)\n").lower()

    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if MENU[f"{answer}"]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there's not enough water.")
        if MENU[f"{answer}"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there's not enough milk.")
        if MENU[f"{answer}"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there's not enough coffee.")

        if (MENU[f"{answer}"]["ingredients"]["water"] <= resources["water"] and MENU[f"{answer}"]["ingredients"]["milk"]
                <= resources["milk"] and MENU[f"{answer}"]["ingredients"]["coffee"] <= resources["coffee"]):
            print(f"Please, insert coins to prepare your {answer}")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            if total >= MENU[f"{answer}"]["cost"]:
                change = round((total - MENU[f"{answer}"]["cost"]), 2)
                profit += MENU[f"{answer}"]["cost"]
                print(f"Here's ${change} in change.")
                print(f"Here's your {answer} ☕. Enjoy it!")
                process_drink()
            elif total < MENU[f"{answer}"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")

    if answer == "off":
        power_on = False

    if answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
