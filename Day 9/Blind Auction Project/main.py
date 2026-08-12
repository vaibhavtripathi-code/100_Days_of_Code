bid_data = {}

bid_again = True
while bid_again:
    name = input("Please enter your name: ")
    bid = int(input("Enter your bid amount $: "))
    bid_data[name] = bid
    print("\n"*100)
    ask = input("Does anyone else want to bid? y/n: ").lower()

    if ask == "y" or ask == "yes":
        continue
    elif ask == 'n' or ask == "no":
        bid_again = False

winner = ''
score = 0
for i in bid_data:
    if bid_data[i] > score:
        score = bid_data[i]
        winner = i

print(f"The winner is {winner} with a bid of ${score}!")