############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import os

def clear_console():
    os.system('cls')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def play_game():

    from art import logo
    print (logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the card."""

        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        if sum(cards) > 11 and 11 in cards:
            cards.remove(11)
            cards.append(1)
                
        return sum(cards)

    def compare(temp_user_score, temp_computer_score):
        if temp_user_score == temp_computer_score:
            print("It's a draw 🙃.")
        elif temp_computer_score == 0:
            print("You Lose, opponent has BlackJack 😱.")
        elif temp_user_score == 0:
            print("You win with a BlackJack 😎.")
        elif temp_user_score > 21:
            print("You went over. You Lose 😭.")
        elif temp_computer_score > 21:
            print("Opponent went over. You win 😁")
        elif temp_user_score > temp_computer_score:
            return "You Win 😊"
        else:
            return "You Lose 😤"

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, Your current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Want to draw another card? Reply 'yes' or 'no'. ")
            if choice == 'yes':
                user_cards.append(deal_card())
            elif choice == 'no':
                is_game_over = True
            else:
                print("Sorry, You inserted wrong input. Please type 'yes' or 'no' only.")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ") == 'y':
    clear_console()
    play_game()

