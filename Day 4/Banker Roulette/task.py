import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
bill = friends[random.randint(0,4)]
print(f"The bill would be paid by {bill}.")

#Alternative way

random.choice(friends)