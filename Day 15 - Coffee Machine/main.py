from drink_menu import MENU
from os import system
from time import sleep
from art import art

# intitial/max resource and total earnings/drinks initialization before starting
INITIAL_RESOURCES = {
    'milk':250,
    'water':250,
    'coffee':10,
    'tea':30,
    'cocoa':30,
    'sugar':30,
}
MAX_RESOURCES = {
    'milk': 250,
    'water': 250,
    'coffee': 10,
    'tea': 30,
    'cocoa': 30,
    'sugar': 30
}
TOTAL_EARNINGS = 0
TOTAL_DRINKS_SERVED = 0
ADMIN_CODE = 99
SWITCH_OFF_CODE = 0

def check_available_ingredients(ingredients_required,item_cost):
    global TOTAL_EARNINGS
    num_of_items_required = 0
    num_of_items_available = 0
    items_not_available = []
    
    for item_name,quantity in ingredients_required.items():
        num_of_items_required += 1
        if ingredients_required[item_name] <= INITIAL_RESOURCES[item_name]:
            
            num_of_items_available += 1
        else:
            items_not_available.append(item_name)
    if num_of_items_available == num_of_items_required:
        for item in ingredients_required.keys():
            INITIAL_RESOURCES[item] -= ingredients_required[item]
        TOTAL_EARNINGS += item_cost
        return True
    else:
        system('clear')
        
        print(f"Sorry, Insufficient ingredients available :")
        for items in items_not_available:
            print(items)
        print(f"\nItem will not be processed, collect your money before trying again..\n")
        return False


def process_coins(item):
    
    item_cost = float(MENU[item]['cost'])
    to_prepare_drink = True
    total_coins = 0
    
    while True:
        try :
            while total_coins < item_cost:
               
                fifty_pence = float(input("How many fifty pence coins? (0.50£) :"))
                fifty_pence *= 0.50
                total_coins += fifty_pence
                
                if total_coins >= item_cost:
                    system("clear")

                    print(f"\nAmount Detected : {total_coins:.2f}£. Thank you!\n")
                    break
                one_pound = float(input("How many one pound coins? (1.00£) :"))
                one_pound *= 1.00
                total_coins += one_pound

                if total_coins >= item_cost:
                    system("clear")
                    
                    print(f"\nAmount Detected : {total_coins:.2f}£. Thank you!\n")
                    break
                else:
                    print(f"\nOnly {total_coins:.2f}£ were detected. Please insert {item_cost-total_coins:.2f}£ more..\n")
                
            sleep(3)
            
            if total_coins >= item_cost:
                if total_coins - item_cost != 0:
                    refund_amt = total_coins - item_cost
                    print(f"{item_cost:.2f}£ has been processed for your {item}, Please collect {refund_amt:.2f}£ before leaving.")
                else:
                    print(f"{item_cost:.2f}£ has been processsed..")
                return True
            else:
                print(f"\nOnly {total_coins:.2f}£ were detected. Please insert {item_cost-total_coins:.2f}£ more..\n")
        except ValueError:
            print("Sorry, Invalid input detected.\n")
            sleep(2)
            print(f"Any money collected will be returned, trying again..\n")
            sleep(3)
            system('clear')


def make_drink(drink_name):
    ingredients_required = MENU.get(drink_name).get('ingredients')
    # print(ingredients_required)
    item_cost = MENU.get(drink_name).get('cost')
    if check_available_ingredients(ingredients_required,item_cost):
        
        print("\nPrepring your drink now!\n")
        sleep(1)
        symbol = ""
        emoji = ["⏳","⌛️","⏳","⌛️","⏳","⌛️"]
        for item in ingredients_required.keys():
            sleep(1.5)
            symbol += "."
            print(f"{emoji[len(symbol)]} Adding {item}{symbol}")
            
        sleep(1)
        print(f"\nHere is your ☕️ {drink_name}, enjoy!")
        sleep(2)
        return True
    return False

def refill_ingredients():
    try:
        while True:
            print("\n====Refill Menu====")
            print("\n1. Refill Milk\n2. Refill Water\n3. Refill Coffee\n4. Refill Tea\n5. Refill Cocoa\n6. Refill Sugar\n7. Exit\n")
            to_refill = int(input("What would you like to refill ? (1-7) :"))
            if to_refill == 1:
                system('clear')
                print("\nRefilling of Milk in process..")
                if INITIAL_RESOURCES["milk"] == MAX_RESOURCES["milk"]:
                    print("\nSorry! Milk is full!")
                else:
                    INITIAL_RESOURCES["milk"] = MAX_RESOURCES["milk"]
            elif to_refill == 2:
                system('clear')
                print("\nRefilling of Water in process..")
                if INITIAL_RESOURCES["water"] == MAX_RESOURCES["water"]:
                    print("\nSorry! Water is full!")
                else:
                    INITIAL_RESOURCES["water"] = MAX_RESOURCES["water"]
                    print("\nWater has been refilled!")
            elif to_refill == 3:
                system('clear')
                print("\nRefilling of Coffee in process..")
                if INITIAL_RESOURCES["coffee"] == MAX_RESOURCES["coffee"]:
                    print("\nSorry! Coffee is full!")
                else:
                    INITIAL_RESOURCES["coffee"] = MAX_RESOURCES["coffee"]
                    print("\nCoffee has been refilled!")
            elif to_refill == 4:
                system('clear')
                print("\nRefilling of Tea in process..")
                if INITIAL_RESOURCES["tea"] == MAX_RESOURCES["tea"]:
                    print("\nSorry! Tea is full!")
                else:
                    INITIAL_RESOURCES["tea"] = MAX_RESOURCES["tea"]
                    print("\nTea has been refilled!")
            elif to_refill == 5:
                system('clear')
                print("\nRefilling of Cocoa in process..")
                if INITIAL_RESOURCES["cocoa"] == MAX_RESOURCES["cocoa"]:
                    print("\nSorry! Cocoa is full!")
                else:
                    INITIAL_RESOURCES["cocoa"] = MAX_RESOURCES["cocoa"]
                    print("\nCocoa has been refilled!")
            elif to_refill == 6:
                system('clear')
                print("\nRefilling of Sugar in process..")
                if INITIAL_RESOURCES["sugar"] == MAX_RESOURCES["sugar"]:
                    print("\nSorry! Sugar is full!")
                else:
                    INITIAL_RESOURCES["sugar"] = MAX_RESOURCES["sugar"]
                    print("\nSugar has been refilled!")
            elif to_refill == 7:
                return
            else:
                print("\nThe item is not available, try again..")
    
    except ValueError:
        print("\nIncorrect input detected! Try again..")

def ingredient_levels():
    print("Current Ingredient Levels :\n")
    for items,quantity in INITIAL_RESOURCES.items():
        if items in ['milk','water']:
            print(f"{items.title()} : {quantity} ml")
        else:
            print(f"{items.title()} : {quantity} gm")
                
def admin():
    
    exit_admin = False
    system('clear')
    while not exit_admin:
        
        try:
            while True:
                
                print("\n====Welcome to Admin Menu====\n")
                print("""1. Current level of ingredients\n2. Refill ingredients\n3. Sales report\n4. Exit\n""")
                admin_option = int(input("What would you like to check ? (1-4) :"))
                system('clear')
                if admin_option == 1:
                    ingredient_levels()
                elif admin_option == 2:
                    ingredient_levels()
                    refill_ingredients()
                    system('clear')
                elif admin_option == 3:
                    print("Sales Report:\n")
                    print("Total Earnings:\n")
                    print(f"{TOTAL_EARNINGS:.2f}£\n")
                    print("Total Drinks Served:\n")
                    print(f"{TOTAL_DRINKS_SERVED}\n")
                elif admin_option == 4:
                    return
                else:
                    system('clear')
                    print("Sorry! The requested function is not available.")
                    
        except ValueError:
            system('clear')
            print("Invalid input! Only numbers allowed.")
            

# ask user what would they like ?
def start():
    global TOTAL_DRINKS_SERVED
    switch_on = True
    print(f"{art}")
    while switch_on:
        menu_idx = 0
        drinks_list = []
        
        try:
            
            print("\n====Drinks Menu====\n")
            for drinks in MENU.keys(): 
                menu_idx+=1
                print(f"{menu_idx}. {drinks} {MENU[drinks]['cost']}","£")
                drinks_list.append(drinks)
            print("")
            user_drink_choice = int(input("What would you like to have? (1-5) :"))
            if 1 <= user_drink_choice <= len(MENU.keys()):
                print("Please the insert required money! We accept following coins (0.50£, 1.00£).\n")
                if process_coins(drinks_list[user_drink_choice-1]):
                    if make_drink(drinks_list[user_drink_choice-1]):
                        TOTAL_DRINKS_SERVED += 1
                        continue
            elif user_drink_choice == ADMIN_CODE:
                admin()
                system('clear')
            elif user_drink_choice == SWITCH_OFF_CODE:
                print("\nThe Coffee Machine is switching off in..\n")
                for _ in range(5,-1,-1):
                    print(f"\r{_}",end="",flush=True)
                    sleep(1)
                print("")
                print("\nSwitched OFF.")
                switch_on = False
            else:
                print("\nSorry! The requested function is not available.")
        except ValueError:
            system('clear')
            print("Invalid input! Only numbers allowed.")

start()
