print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


bill_amount = bill + (bill * tip/100)
split = round(bill_amount / people,2)

print(f"For {people} people, each person should pay ${split}")


