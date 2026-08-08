import art
# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(dir, original_text, shift_amount):
    new_word = ''
    if dir == 'decode':
        shift_amount *= -1
    for i in original_text:
        if i in alphabet:
            prev_index = alphabet.index(i)
            new_word += alphabet[(prev_index + shift_amount) % 26]
        else:
            new_word += i
    if dir == 'encode':
        print(f"Your encoded message is '{new_word}'")
    elif dir == 'decode':
        print(f"Your decoded message is '{new_word}'")


# TODO-3: Can you figure out a way to restart the cipher program?
loop_run = True
while loop_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    print("----------------------------------------------------------------------")
    ask_loop = input("\nDo you want to run the program again? y/n: ").lower()
    if ask_loop == 'n' or ask_loop == 'no':
        loop_run = False
    elif ask_loop == 'y' or ask_loop == 'yes':
        loop_run = True


