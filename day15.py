# coffee machine

MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "coins": 1.5
    },
     "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "coins": 2.5
    }, 
     "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "coins": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
    
}
def resource_sufficient(order):
    for i in order:
        if order[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    print("Insert coins")
    total = int(input("How  many quarters?: ")) *0.25
    total += int(input("How  many dimes?: ")) *0.1
    total += int(input("How  many nickles?: ")) *0.05
    total += int(input("How  many pennies?: ")) *0.01
    return total

def transaction(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"here is ${change} the change")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money.")
        return False
    
    
def make_coffee(drink, order):
    for i in order:
        resources[i]-=order[i]
    print(f"Here is your drink 💕")
        
        
on = True
profit = 0 
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["coins"]):
                make_coffee(choice, drink["ingredients"])
                print(drink)

         