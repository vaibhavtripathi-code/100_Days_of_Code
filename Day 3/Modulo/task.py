#Pause 1
print(10%3) #it should be 1

#Pause 2
print("Even and Odd Checker")
try:
    number = int(input("Enter a number to check: "))
    if number % 2 == 0:
        print("Even")
    elif number % 2 != 0:
        print("Odd")

except ValueError:
    print("Please enter an integer")

