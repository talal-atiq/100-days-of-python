#importing modules
from data import MENU, resources, logo, resources_art

##############################################################################################
#Functions:
def resource_check(order):
    if MENU[order]['ingredients']['water'] <= resources['water']:
        if MENU[order]['ingredients']['coffee'] <= resources['coffee']:
            if order == 'espresso':
                return True
            elif order == 'latte' or order == 'cappuccino':
                if MENU[order]['ingredients']['milk'] <= resources['milk']:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

################################################################################################
def money_return( money ):
    if money >= MENU[order]['cost']:
        amount = money - MENU[order]['cost']
        return 1
    else:
        return 0

####################################################################################################
def coffee_making(order):
    if order == "espresso":
        resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
        return f"There you go with a freshly prepared cup of {order} coffee.\nKeep Gulping the Caffeine"
    else:
        resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
        resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
        return f"There you go with a freshly prepared cup of {order} coffee.\nKeep Gulping the Caffeine"
##################################################################################################################
def again():
    should_continue = input("Would you like to have one more cup of coffee? (yes/no)\n").lower()
    if should_continue == "yes":
        return True
    else:
        return False

########################################################################################################

exit = False
while not exit:
    print(logo)
    print("Welcome to virtual cofffee, How can i help you?\n")
    print(resources_art)
    milk = resources['milk']
    coffee = resources['coffee']
    water = resources['water']
    print(f"We currently have:\nMilk: {milk}ml\nCoffee: {coffee}g\nWater: {water}ml")
    order = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    print("Please enter the money tokens below\n")
    quarter = int(input("Quarters:  ")) * 0.25
    dime = int(input("Dimes:  ")) * 0.10
    nickel = int(input("Nickels:  ")) * 0.05
    penny = int(input("Pennies:  ")) * 0.01
    money = round(quarter + dime + nickel + penny, 2)
    in_return = money_return(money)
    if in_return == 0:
        print(f"Sorry, not enough money to buy {order} coffee")
        exit = True
    else:
        change = money - MENU[order]['cost']
        print(f"Here's your change = {change}$")
    available_resources = resource_check(order)
    if available_resources:
        coffee = coffee_making(order)
        print(coffee)
        exit = False
    else:
        print("Not sufficient resources!")
        exit = True
    again = again()
    if again:
        exit = False
    else:
        exit = True


input()





