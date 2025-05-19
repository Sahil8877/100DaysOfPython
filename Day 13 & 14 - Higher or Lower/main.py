from movie_data import movie_data
from random import choice
import textwrap,os
from art import verses_art

def random_movie_generators(movie_data):
    """
    Generates two random movies and returns their earnings, description as a dictionary 
    {
    movie_name(str):
        {
        earnings(int):earnings,
        description(str):description
        }
    }
    """
    movies = list(movie_data)
    movie_earnings_and_description = {}
    same_movie = ""
    
    for _ in range(2):
        random_movie = choice(movies)
        while random_movie == same_movie:
            # to avoid duplicate movies
            random_movie = choice(movies)
        fetched_movie_earnings = movie_data[random_movie]['Gross']
        fetched_movie_description = movie_data[random_movie]['Description']
        movie_earnings_and_description[random_movie] = {'earnings':fetched_movie_earnings,'description':fetched_movie_description}
        same_movie = random_movie  
    return movie_earnings_and_description

def score_calculator(user_guess,in_game_movie_info,in_game_movie_names):
    """
    Calulcate the current score using:
    `user_guess`:str,
    `in_game_info`:dict,
    `in_game_movie_names`:list
    if the highest grossing movie and user guess is equal return True, return False otherwise.
    """
    a = in_game_movie_info[in_game_movie_names[0]]['earnings']
    b = in_game_movie_info[in_game_movie_names[1]]['earnings']
    movie_with_higher_earnings = max(a,b)

    if movie_with_higher_earnings == a and user_guess == 'a':
        return True
    elif movie_with_higher_earnings == b and user_guess == 'b':
        return True
    return False

def game_exit():
    """
    ask user choice to play again otherwise return False
    """
    choice = 'y'
    while choice != 'n':
        choice = input("Would like to play again? (y/n) :").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("\nQuitting Game..")
            return False
        else:
            print("\nWrong input, try again..")


def get_user_guess():
    """
    ask user to guess and return user guess if user guesses either 'a' or 'b'.
    """
    while True:
        user_guess = input("\nWhich movie has higher box office numbers? Type 'A' or 'B': ").lower()
        if user_guess == 'a' or user_guess == 'b':
            return user_guess
        else:
            print("\nIncorrect input! Please enter 'A' or 'B'.")


def main():
    os.system('clear')
    print("\nHigher or Lower : With Movies\n")
    playing = True
    current_score = 0

    while playing:

        in_game_movie_info = {}
        in_game_movie_names = []
        for key,value in random_movie_generators(movie_data).items():
            #Populate in_game_movie_info with selected random movie info like - name,earnings and description
            in_game_movie_info[key] = value
            #Populate in_game_movie_names with movie names using keys from the random_movie_generator() dict
            in_game_movie_names.append(key)
  
        description_movie_A = in_game_movie_info[in_game_movie_names[0]]['description']
        description_movie_B = in_game_movie_info[in_game_movie_names[1]]['description']
        
        print(f"Compare A : \n\n{in_game_movie_names[0]}:")
        print(textwrap.fill(f"{description_movie_A}",width=80))
        print(f"{verses_art}")
        print(f"\nAgainst B : \n\n{in_game_movie_names[1]}:")
        print(textwrap.fill(f"{description_movie_B}",width=80))
        user_guess = get_user_guess()
        scored = score_calculator(user_guess,in_game_movie_info,in_game_movie_names)
        if scored:
            current_score += 1
            os.system('clear')
            print("Current Score :",current_score,"\n")
        elif not scored:
            os.system('clear')
            print(f"\nGotcha!!\nGame Over, You chose the wrong movie.\nYour Score was :",current_score,"\n")
            if game_exit():
                playing = True
                os.system('clear')
            else:
                playing = False

main()
