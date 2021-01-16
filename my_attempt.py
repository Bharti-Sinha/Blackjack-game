import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
dealer = []


def deal(player):
    player.append(random.choice(cards))


def computer():
    while sum(dealer) < 17:
        deal(dealer)

    if sum(dealer) == 21:  # added this - Rushi
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("Computer had a black jack, You lose!")
        choice()

    if sum(dealer) > 21:
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("Computer lose")
        choice()

    elif sum(dealer) > sum(user):
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("You lose")
        choice()

    elif sum(dealer) < sum(user):
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("You Win")
        choice()

    else:
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("It's a Draw!")
        choice()


def status():
    print(user)
    print(sum(user))
    print(dealer)
    print(sum(dealer))


def start_game():
    # check if computer has blackjack
    if sum(dealer) == 21:
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("Computer had a black jack, You lose!")
        choice()

    # check if the user has blackjack
    elif sum(user) == 21:  # this was previously sum(dealer) changed it! - Rushi
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer final hand: {dealer}, current score: {sum(dealer)}")
        print("You had a black jack, You Win!")
        choice()

    # play game
    else:
        print("neither have blackjack")
        if sum(user) > 21:
            print("Sum of user is >21")
            if 11 in user:
                user[user.index(11)] = 1
                if sum(user) > 21:
                    print(f"Your cards: {user}, current score: {sum(user)}")
                    print(f"Computer first card: {dealer[0]}")
                    print('You lose')
                    choice()
                elif sum(user) == 21:
                    status()
                    print('BLACKJACK! You win!')
                    choice()
                else:  # addded this condition - Rushi
                    start_game()
            else:

                print(f"Your cards: {user}, current score: {sum(user)}")
                print(f"Computer first card: {dealer[0]}")
                print("You lose")
                choice()

        if sum(user) < 21:
            print("Sum of user <21")
            print(f"Your cards: {user}, current score: {sum(user)}")
            print(f"Computer first card: {dealer[0]}")
            next_move = input("Type 'y' to draw another card, type 'n' to pass ").lower()
            if next_move == 'y':
                deal(user)
                status()
                start_game()
            elif next_move == 'n':
                status()
                computer()
            else:  # added this condition - Rushi
                print("Please enter a valid input. Type 'y' or 'n'.")
                start_game()


def choice():
    inp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if inp == 'y':
        global cards
        global user
        global dealer
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user = []
        dealer = []
        for i in range(0, 2):
            user.append(random.choice(cards))
            dealer.append(random.choice(cards))
        start_game()
    if inp == 'n':  # added this condition - Rushi
        print("Thank you for wasting time!")
        print("Created by: Bharti Sinha")


choice()
