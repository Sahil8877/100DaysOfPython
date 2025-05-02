import random
print("\n** H A N G M A N **")
#random word bank
Wordlist = Wordlist = [
    'apple',
    'banana',
    'mango',
    'grape',
    'orange',
    'strawberry',
    'peach',
    'pineapple',
    'pear',
    'kiwi',
    'papaya',
    'blueberry',
    'cherry',
    'watermelon',
    'plum',
    'apricot',
    'lemon',
    'lime',
    'coconut',
    'pomegranate'
]
RED = "\033[91m" #ANSI art red
RESET = "\033[0m"
#random messages list
messages = [
    "Oh! you got that right..",
    "You are SMART!!",
    "You are on the right track..",
    "Absolutely correct!",
    "Nailed it!",
    "That's spot on!",
    "Great job!",
    "You're thinking like a pro!",
    "Exactly!",
    "Bingo! You got it!"
]
#hangman drawing with ANSI art
hangman_level = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
      |
      |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
  {RED}|{RESET}   |
      |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
 {RED}/{RESET}{RED}|{RESET}   |
      |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
 {RED}/{RESET}{RED}|{RESET}{RED}\{RESET}  |
      |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
 {RED}/{RESET}{RED}|{RESET}{RED}\{RESET}  |
 {RED}/{RESET}    |
      |
=========''', f'''
  +---+
  |   |
  {RED}O{RESET}   |
 {RED}/{RESET}{RED}|{RESET}{RED}\{RESET}  |
 {RED}/{RESET} {RED}\{RESET}  |
      |
=========''']

random_word = random.choice(Wordlist)


length_of_selected_word = len(random_word)



print(f"\nWord Hint: Fruit with {length_of_selected_word} letters")

blank_string = "_"*length_of_selected_word
list_with_blanks = list(blank_string)

print("".join(list_with_blanks))

user_guesses = set()
play = True
hang_level = 0


while play:
        current_string = "" #string to store in game state of letters 
        if hang_level == 6: 
            play = False #play variable set to False
            print("\n"+hangman_level[hang_level])
        else:
            user_guess = input("\nGuess the letters : ").lower() #user guesses letter in lowercase
            if user_guess in user_guesses: #if the user guessed letter in user_guesses
                print("🥱 Oho! The letter was already guessed, try again.")
                print(hangman_level[hang_level])
                continue
            if user_guess in random_word: #if the guessed letter is present in randomly selected word
                for letter in random_word: #iterate on each letter
                    if letter == user_guess: 
                        current_string += letter #if letter matches user input then add it to the string 
                        user_guesses.add(letter) #user_guesses variable to keep track of previous letters
                        
                    elif letter in user_guesses: #if letter was present in user_guesses variable
                        current_string += letter # we add the new letter to the string
                    else:
                        current_string += "_" #if no letters are matched then the string will have empty blanks
            else:
                    hang_level += 1 #if the user gussed wrong letters add hangman level with 1
                    if hang_level < 6: #check if hangman level is inbound
                        print(f"\n🙈 Uhho! Wrong letter.\nTry again!")
                        print("\n"+hangman_level[hang_level])
                        continue #program continues 
            if hang_level < 6: 
                print("\n"+current_string)
                random_message = random.choice(messages) #random messages from message list
                print(f"\n{random_message}")
                print("\n"+hangman_level[hang_level])
            if current_string == random_word: #winning condition
                print(f"\n🎖️ Awesome! You did it. The word was {random_word}.")
                break #end while loop
else:
    print("Game Over") #game over when play = False
        