import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares scores between users cards and computers cards"""
    if user_score > 21 and computer_score > 21:
        return "Bust! you lose!"
    if user_score == computer_score:
        return "Draw🥴"
    elif computer_score == 0:
        return "You Lose🤢"
    elif user_score == 0:
        return "You Win! BlackJack!💰"
    elif user_score > 21:
        return "You have over 21! BUST!😭"
    elif computer_score > 21:
        return "Dealer has over 21! BUST!💰"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"


def game_start():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}   Your score {user_score}")
        print(f"    Dealers cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_hit = input("Type 'y' to hit, type 'n' to pass: ")
            if user_hit == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards} & Final score: {user_score}")
    print(f"    Dealer's final hand {computer_cards} & Final score: {computer_score}")
    print(compare(user_score, computer_score))

    play_game = input("Would you like to play a game of Blackjack? Type 'y' for yes 'n' for no: ")
    while play_game == 'y':
        game_start()


play_game = input("Would you like to play a game of Blackjack? Type 'y' for yes 'n' for no: ")
while play_game == 'y':
    game_start()