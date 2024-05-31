# Day 8 of 100 Days of Code: Caesar Cipher

from caesar_cipher_art import logo
print(logo)
play_again = True

while play_again: #used to replay the game if option selected by user
  
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # handling user input > 26, using modulus to reduce the number to one which works with the alphabet list above (i.e. a shift of 30 is the same as a shift of 4)
  if shift > 26:
    shift = shift % 26
  
  def caesar(raw_text, shift_amount, cipher_direction):
    finished_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for letter in raw_text:
      if letter not in alphabet: #used to handle other characters e.g. 12 3!? and not wanting them to be encoded/decoded
        finished_text += letter
      else:
        letter_position = alphabet.index(letter)
        new_letter_position = letter_position + shift_amount
        finished_text += alphabet[new_letter_position]
    print(f"The {cipher_direction}d text is {finished_text}")

  
  caesar(raw_text = text, shift_amount = shift, cipher_direction = direction)

  # option to play again
  continue_game = input("Would you like to go again. Type 'yes' or 'no'.\n").lower()
  if continue_game == "no":
    play_again = False
    print("Thanks for using Caesar Cipher. Goodbye!")