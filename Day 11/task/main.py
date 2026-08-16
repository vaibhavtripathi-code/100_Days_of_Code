import random

input("Press enter to begin the game of BlackJack!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
computer_hand = []

player_score = 0
computer_score = 0

replay = True
def deal():
    player_score = 0
    computer_score = 0
    if len(player_hand) < 2:
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
    elif len(player_hand) >= 2:
        player_hand.append(random.choice(cards))
    player_score += sum(player_hand)

    if sum(computer_hand) < 17:
        computer_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        computer_score += sum(computer_hand)
    else:
        pass
    return player_hand, computer_hand, player_score, computer_score

while replay:
    computer_hand, player_hand, player_score, computer_score = deal()
    def win_or_lose(player_hand, computer_hand, player_score, computer_score):
        print("Player hand: ", player_hand, "Your Score: ", player_score)
        print("Computer hand: ", computer_hand[0])

        if player_score > 21 and computer_score < 21:
            print("Bust! You Lose 😭")
        elif computer_score > 21 and player_score < 21:
            print("BlackJack! You Win! 🥳")
    hit_ask = input("Do you want to draw again? y/n: ")

    win_or_lose(player_hand, computer_hand, player_score, computer_score)

    if hit_ask == "y":
        deal()
    elif hit_ask == "n":
        replay = False
