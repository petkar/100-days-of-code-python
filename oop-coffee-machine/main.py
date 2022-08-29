from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def input_coffee(menu, machine, atm):
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        return menu.find_drink(prompt)
    elif prompt == "off":
        quit()
    elif prompt == "report":
        machine.report()
        atm.report()
        return input_coffee(menu, machine, atm)
    else:
        print("Please enter a valid option.")
        return input_coffee(menu, machine, atm)


def main():
    machine = CoffeeMaker()
    menu = Menu()
    atm = MoneyMachine()
    while True:
        options = menu.get_items()
        drink = input_coffee(menu, machine, atm)
        if machine.is_resource_sufficient(drink) and atm.make_payment(drink.cost):
            machine.make_coffee(drink)


if __name__ == "__main__":
    main()
