print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("You pay $5.")
        bill = 5
    elif age <= 18:
        print("You pay $7.")
        bill = 7
    else:
        print("You pay $12.")
        bill = 12
    photo = input("Do you also want a photo to be taken? y/n: ")
    if photo == "y":
        bill += 3
    print(f'Your final bill is: ${bill}')
else:
    print("Sorry you have to grow taller before you can ride.")
