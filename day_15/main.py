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


# 4. Check resources sufficient?

def check_resources(user_choice):
    item_menu = MENU[user_choice]['ingredients']
    for ingredient in item_menu:
        if not resources[ingredient] >= item_menu[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


#  7. Make Coffee.

def make_coffee(user_choice):
    item_menu = MENU[user_choice]['ingredients']
    global resources
    for ingredient in item_menu:
        resources[ingredient] -= item_menu[ingredient]
    print(f"Here is your {user_choice} ☕ Enjoy!")


# 5. Process coins.

def check_coins(user_choice):
    item_cost = MENU[user_choice]['cost']
    global resources
    print("Please insert coins.")
    payed_amount = int(input("How many quarters?: ")) * 0.25
    payed_amount += int(input("How many dimes?: ")) * 0.10
    payed_amount += int(input("How many nickles?: ")) * 0.05
    payed_amount += int(input("How many pennies?: ")) * 0.01

    if payed_amount > item_cost:
        print(f"Here is ${"{:.2f}".format(payed_amount - item_cost)} in change.")
        resources['money'] += item_cost
        return True
    elif payed_amount == item_cost:
        print("Thank you.")
        resources['money'] += item_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# 3. Print report.


def create_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")

# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"


def coffee_maker():
    status_on = True
    global resources
    resources['money'] = 0.0
    while status_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "report":
            create_report()
        elif user_choice == "off":
            # 2. Turn off the Coffee Machine by entering “off” to the prompt
            print("turning device off, goodbye!")
            status_on = False
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            if check_resources(user_choice):
                if check_coins(user_choice):
                    make_coffee(user_choice)


coffee_maker()
