import random, os, time

cards = {
    'A': 11,
    'J': 10,
    'K': 10,
    'Q': 10,
    'num_cards': [2, 3, 4, 5, 6, 7, 8, 9, 10]
}

dealer_has = []
player_has = []

def score_calculator(cardlist):
    score = 0
    ace_count = 0
    for card in cardlist:
        if str(card).isdigit():
            score += int(card)
        elif card == 'Q' or card == 'K' or card == 'J':
            score += 10
        elif card == 'A':
            ace_count += 1

    for i in range(ace_count):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1

    return score

def random_card_generator(num_of_cards_to_draw, dealer_or_player):
    global dealer_has, player_has
    for i in range(num_of_cards_to_draw):
        random_card_type_selection = random.choice(list(cards))
        if random_card_type_selection == 'num_cards':
            random_card_type_selection = random.choice(list(cards['num_cards']))
            if dealer_or_player == 'dealer':
                dealer_has.append(random_card_type_selection)
            else:
                player_has.append(random_card_type_selection)
        else:
            if dealer_or_player == 'dealer':
                dealer_has.append(random_card_type_selection)
            else:
                player_has.append(random_card_type_selection)
    if dealer_or_player == 'dealer':
        return dealer_has
    else:
        return player_has

def dealer_card_selection(num_of_cards_to_draw_by_dealer):
    global dealer_has
    dealer_has = random_card_generator(num_of_cards_to_draw_by_dealer, dealer_or_player='dealer')
    return dealer_has

def player_cards_selection(num_of_cards_to_draw_by_player):
    global player_has
    player_has = random_card_generator(num_of_cards_to_draw_by_player, dealer_or_player='player')
    print("🃏 You drew: ", player_has[-num_of_cards_to_draw_by_player:])
    print("🧮 Your current hand:", player_has)
    print("📊 Your current score:", player_score_checker())
    return player_has

def dealer_score_checker():
    global dealer_has
    dealer_score = score_calculator(dealer_has)
    return dealer_score

def player_score_checker():
    global player_has
    player_score = score_calculator(player_has)
    return player_score

def print_push(dealer_score, player_score):
    if dealer_score == player_score:
        print("\n🤝 It's a PUSH! You and the dealer have the same score.")
        print("📜 Dealer's full hand:", dealer_has)
        print("🧮 Dealer's score:", dealer_score)
        print("🧮 Your score:", player_score)
        return True
    else:
        return False

def check_winning_condition(dealer_or_player, hit_or_stand):
    dealer_score = dealer_score_checker()
    player_score = player_score_checker()
    player_won = 0
    dealer_won = 0
    if dealer_or_player == 'dealer':
        if len(dealer_has) == 2 and dealer_score == 21:
            print("\n💥 Dealer hits BLACKJACK! You lose.")
            print("📜 Dealer's hand:", dealer_has)
            print("🧮 Dealer's score: 21")
            dealer_won = 1
        elif dealer_score > player_score:
            print("\n😞 You lose! Dealer has a higher score.")
            print("📜 Dealer's hand:", dealer_has)
            print("🧮 Dealer's score:", dealer_score)
            print("🧮 Your score:", player_score)
            dealer_won = 1
        return dealer_won
    else:
        if player_score > dealer_score and hit_or_stand == 's':
            print("\n🎉 You win! Your score beats the dealer.")
            print("📜 Dealer's hand:", dealer_has)
            print("🧮 Dealer's score:", dealer_score)
            print("🧮 Your score:", player_score)
            player_won = 1
        elif player_score < 21:
            player_won = 0
        return player_won

def play_rounds(player_score, dealer_score):
    playing = True
    while playing:
        if player_score < 21:
            hit_or_stand = input("To hit another card press 'H' or press 'S' to take a stand :").lower()
            print("")
            if hit_or_stand == 'h':
                print("➕ You chose to hit!")
                player_cards_selection(num_of_cards_to_draw_by_player=1)
                player_score = player_score_checker()
                dealer_score = dealer_score_checker()
                if print_push(dealer_score, player_score):
                    return False
            elif hit_or_stand == 's':
                print("🙋‍♂️ You chose to stand.")
                player_score = player_score_checker()
                dealer_score = dealer_score_checker()
                if print_push(dealer_score, player_score):
                    return False
                while dealer_score < 17:
                    print("🂠 Dealer draws a card...")
                    time.sleep(1)
                    dealer_card_selection(num_of_cards_to_draw_by_dealer=1)
                    dealer_score = dealer_score_checker()
                dealer_won = check_winning_condition(dealer_or_player='dealer', hit_or_stand='')
                player_won = check_winning_condition(dealer_or_player='player', hit_or_stand='s')
                if dealer_score > 21:
                    print("\n🔥 Dealer busts! You win.")
                    print("📜 Dealer's hand:", dealer_has)
                    print("🧮 Dealer's score:", dealer_score)
                    return False
                if dealer_won == 1:
                    return False
                elif player_won == 1:
                    return False
            else:
                print("❌ Invalid input. Please enter 'h' or 's'.\n")
        if len(player_has) >= 2 and player_score == 21:
            print("\n🃏 BLACKJACK! You win!")
            print("📜 Dealer's hand:", dealer_has)
            print("🧮 Dealer's score:", dealer_score)
            print("🧮 Your score: 21")
            return False
        elif player_score > 21:
            print("\n💣 You busted! Score over 21.")
            print("🧮 Your final score:", player_score)
            return False
    return True

def play():
    playing = True
    player_score = 0
    while playing:
        user_choice = input("Would you like to play BlackJack ? y/n :").lower()
        if user_choice == 'y':
            os.system('clear')
            print("===🃏 B L A C K J A C K 🃏===\n")
            player_cards_selection(num_of_cards_to_draw_by_player=2)
            player_score = player_score_checker()
            dealer_card_selection(num_of_cards_to_draw_by_dealer=2)
            dealer_score = dealer_score_checker()
            print("🙈 Dealer's 1st card:", dealer_has[0])
            while play_rounds(player_score, dealer_score):
                pass
            
            player_has.clear()
            dealer_has.clear()
        elif user_choice == 'n':
            os.system('clear')
            print("🔁 Quitting game...")
            print("\n👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.\n")

play()
