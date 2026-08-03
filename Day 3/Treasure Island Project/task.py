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

print("You are at crossroads, do you wanna go left or right?")
road = input()
if road == "left" or 'Left':
    print("You reached a river of blood!, Do you wanna swim or wait?")
    river = input()
    if river == "wait" or "Wait":
        print("Congrats! You died in a landslide.")
    elif river == "swim" or "Swim":
        print('You see orbs in front of you. Which one do you want to inspect? red/yellow/blue')
        orb = input()
        if orb == 'red' or 'Red':
            print("The orb glows brighter every second and melts you!")
        elif orb == 'blue' or 'Blue':
            print("The ground below you disappeared and you fell to your abyss!")
        elif orb == 'yellow' or 'Yellow':
            print("Congrats! You win a 0 skill game that gives no reward.")
        else:
            print("Really?")
    else:
        print("Smartest player ever!")
elif road == "right" or "Right":
    print("You were eaten by a hentai monster!")
else:
    print("Can you read?")
