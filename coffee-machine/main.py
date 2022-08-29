MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "profit": 0.0,
}


def input_coffee():
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        return prompt
    elif prompt == "off":
        quit()
    elif prompt == "report":
        print_report()
        return input_coffee()
    else:
        print("Please enter a valid option.")
        return input_coffee()


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def check_resources(coffee):
    can_make = True
    for item in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            can_make = False
    return can_make


def get_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def check_coins(amount, coffee):
    return amount >= MENU[coffee]["cost"]


def process_transaction(amount, coffee):
    cost = MENU[coffee]["cost"]
    resources["profit"] += cost

    change = round(amount - cost, 2)
    print(f"Here is ${change} in change.")


def make_coffee(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    print(f"Here is your {coffee} ☕️. Enjoy!")


def main():
    while True:
        drink = input_coffee()
        inserted_amount = get_coins()
        if check_resources(drink):
            if check_coins(inserted_amount, drink):
                process_transaction(inserted_amount, drink)
                make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")


if __name__ == "__main__":
    main()
