import random,os
from logo import art

def random_num_generator():
    random_num = random.randrange(0,100)
    return random_num

def hard_level(num):
    attempts = 5
    print(f"You have {attempts} attempts to guess the number correctly..\n")
    while attempts > 0:
        user_guess = input("Guess the correct number from 1-100 :")
        if user_guess.isnumeric():
            if int(user_guess) > num:
                attempts -= 1
                print("\n🐌 Slow down buddy! lower your guess..")
                print(f"You have {attempts} attempts to guess the number correctly..\n")
            elif int(user_guess) < num:
                attempts -= 1
                print("\n👀 Look out! you need to aim higher..")
                print(f"You have {attempts} attempts to guess the number correctly..\n")
            elif int(user_guess) == num:
                attempts = 0
                print(f"\n🎉 Voila! You guessed it right, the number was {num}.")
                return True
        else:
            print("Wrong input, Try again!")
    if attempts == 0:
        print(f"Sorry! Game over. The number was {num}.")

def easy_level(num):
    attempts = 10
    print(f"You have {attempts} attempts to guess the number correctly..\n")
    while attempts > 0:
        user_guess = input("Guess the correct number from 1-100 :")
        if user_guess.isnumeric():
            if int(user_guess) > num:
                attempts -= 1
                print("\n🐌 Slow down buddy! lower your guess..")
                print(f"You have {attempts} attempts to guess the number correctly..\n")
            elif int(user_guess) < num:
                attempts -= 1
                print("\n👀 Look out! you need to aim higher..")
                print(f"You have {attempts} attempts to guess the number correctly..\n")
            elif int(user_guess) == num:
                attempts = 0
                print(f"\n🎉 Voila! You guessed it right, the number was {num}.")
                return True
        else:
            print("Wrong input, Try again!\n")
    if attempts == 0:
        print(f"Sorry! Game over. The number was {num}.")
        
def want_to_continue():
    playing = True
    while playing:
        user_choice = input("\nWould you like to retry ? (y/n) :").lower()
        if user_choice == 'y':
            os.system('clear')
            return True
        elif user_choice == 'n':
            os.system('clear')
            print("Thank You.\n")
            return False
        else:
            print("\nSorry! invalid input.")

def play():
    game_over = False 
    while not game_over:
        random_num = random_num_generator()
        print(f"{art}\n")
        difficulty_level = input("Choose level by typing 'easy' or 'hard' :").lower()
        if difficulty_level == 'easy':
            if easy_level(random_num):
                game_over = True
        elif difficulty_level == 'hard':
            if hard_level(random_num):
                game_over = True
        else:
            print("\nWrong input!")
        if want_to_continue():
            game_over = False
        else:
            game_over = True
           
play()
