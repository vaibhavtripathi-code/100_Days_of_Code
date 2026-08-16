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
    player_lose = False
    player_hand, computer_hand, player_score, computer_score = deal()
    def win_or_lose(player_hand, computer_hand, player_score, computer_score):
        print("Player hand: ", player_hand, "Your Score: ", player_score)
        print("Computer hand: ", computer_hand)

        if player_score > 21:
            print("Bust! You Lose 😭")
            return False
        elif computer_score > 21 and player_score < 21:
            print("BlackJack! You Win! 🥳")
            return True
        elif player_score == 21 and player_score != computer_score:
            print("Your Win!")
            return True
        elif computer_score == 21:
            print("Computer Win!")
            return False
        elif player_score == computer_score:
            print("It's a draw!")
            return False


    win_or_lose(player_hand, computer_hand, player_score, computer_score)
    if win_or_lose == True or player_score < 21:
        hit_ask = input("Do you want to draw again? y/n: ")
        if hit_ask == "y":
            player_hand, computer_hand, player_score, computer_score = deal()
            win_or_lose(player_hand, computer_hand, player_score, computer_score)
        elif hit_ask == "n":
            win_or_lose(player_hand, computer_hand, player_score, computer_score)
    else:
        break

# Make a flowchart first, then attempt to make this.


