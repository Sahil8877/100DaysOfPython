import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock,paper,scissors]
print("Welcome to Rock, Paper and Scissors game.\n")
user_choice = int(input("""Please input any of the following :\n
0 for Rock\n1 for Paper\n2 for Scissors\nType here :"""))
random_choice = random.choice(options)

if user_choice == 0: #rock
    print("\nYour move :\n",rock,"\n")
    print("Game move :\n",random_choice,)
    if random_choice == scissors:
        print("You Won!")
    elif random_choice == rock:
        print("It's a Tie!")
    else:
        print("You Lose!")
elif user_choice == 1: #paper
    print("Your move :\n",paper,"\n")
    print("Game move :\n",random_choice,)
    if random_choice == paper:
        print("It's a Tie!")
    elif random_choice == rock:
        print("You Won!")
    else:
        print("You Lose!")
elif user_choice == 2: #scissors
    print("Your move :\n",scissors,"\n")
    print("Game move :\n",random_choice,)
    if random_choice == scissors:
        print("It's a Tie!")
    elif random_choice == paper:
        print("You Won!")
    else:
        print("You Lose!")
