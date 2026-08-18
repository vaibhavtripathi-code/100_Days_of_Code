from art import logo
print(logo)
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Computer has Blackjack! Computer wins!"
    elif user_score == 0:
        return "You have Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. Computer wins!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'yes' to get another card, 'no' to pass: ")
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
play_game()