print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

win = 0
tries = 0
while win == 0:
    tries += 1
    if tries > 1 and tries < 5:
        print("Let's try that again.")
    elif tries >= 5:
        print("Pathetic! Try again.")
    print("You are at a crossroads. Do you want to go left or right?")
    road = input()
    if road == "left" or road == "Left":
        print("You reached a river of blood! Do you want to swim or wait?")
        river = input()
        if river == "wait" or river == "Wait":
            print("Congrats! You died in a landslide.")
        elif river == "swim" or river == "Swim":
            print("You see orbs in front of you. Which one do you want to inspect? Red/Yellow/Blue")
            orb = input()
            if orb == "red" or orb == "Red":
                print("The orb glows brighter every second and melts you. Game Over!")
            elif orb == "blue" or orb == "Blue":
                print("The ground below you disappears, and you fall into the abyss. Game Over!")
            elif orb == "yellow" or orb == "Yellow":
                print("Congrats! You win a zero-skill game, and the real treasure was the friends"
                      " you made along the way.")
                win = 1
            else:
                print("Really?")
        else:
            print("Smartest player ever!")
    elif road == "right" or road == "Right":
        print("You were eaten by a hentai monster. Game Over!")
    else:
        print("Can you read?")

