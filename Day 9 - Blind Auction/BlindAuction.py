from art import art
import random,os
print("\n"+art+"\n")
auctioners = {}
auctioning = True
items = ['car','bike','bycyle','house','gold']
bidding_item = random.choice(items).capitalize()
print(f"\nThis auction is for {bidding_item}.\n")

def start_bid():
    
    user_choice = input("What is your name? :")
    bid_amt = input("Enter the amount you want to bid : $")
    
    if bid_amt.isdigit() == True:
        bid_amt = int(bid_amt)
        if bid_amt > 0:
            auctioners[user_choice] = bid_amt
        else:
            print("\n***Invalid input! Only positive numbers.***\n")
            start_bid()
    else:
        print("\n***Invalid input! Only numbers allowed.***\n")
        start_bid()
    

def winner():
    bid_winner = ""
    highest_bid_amt = max(auctioners.values())
    for key, values in auctioners.items():
        if values == highest_bid_amt:
            bid_winner = key
    return bid_winner


start_bid()
while auctioning:

    user_choice = input("\nDo you have other bidders ? y/n :").lower()
    if user_choice == 'y' or user_choice == 'n':
        if user_choice == 'y':
            os.system("clear")
            print(f"\nThis auction is for {bidding_item}.\n")
            start_bid()
        elif user_choice == 'n':
            print(f"\nThe {bidding_item} goes to {winner().capitalize()}, with a bid of {auctioners[winner()]}$.")
            auctioning = False
    else:
        print("\n***Invalid Input!***\n")