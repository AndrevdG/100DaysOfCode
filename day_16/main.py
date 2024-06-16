from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
register = MoneyMachine()
status_on = True
while status_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        register.report()
    elif user_choice == "off":
        print("turning device off, goodbye!")
        status_on = False
    else:
        menu_item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            if register.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
