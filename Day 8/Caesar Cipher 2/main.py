alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(dir, original_text, shift_amount):
    new_word = ''
    if dir == 'decode':
        shift_amount *= -1
    for i in original_text:
        prev_index = alphabet.index(i)
        new_word += alphabet[(prev_index + shift_amount) % 26]
    if dir == 'encode':
        print(f"Your encoded message is '{new_word}'")
    elif dir == 'decode':
        print(f"Your decoded message is '{new_word}'")
caesar(direction, text, shift)


