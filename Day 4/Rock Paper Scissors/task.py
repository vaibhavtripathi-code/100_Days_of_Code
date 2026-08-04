rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
while True:
    hands = [rock,paper,scissors]
    choice = int(input("Enter 0 for Rock\nEnter 1 for Paper\nEnter 2 for Scissors\n"))
    compchoice = random.randint(0,2)
    print("CPU Choice")
    print(hands[compchoice])
    print("Your Choice")
    print(hands[choice])
    if choice == compchoice:
        print("It's a draw!")
    elif choice == 0 and compchoice == 2:
        print("You win!")
    elif choice == 1 and compchoice == 0:
        print("You win!")
    elif choice == 2 and compchoice == 1:
        print("You win!")
    else:
        print("You lose!")



