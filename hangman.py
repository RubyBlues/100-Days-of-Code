# Day 7 of 100 Days of Code: Hangman

import random
from hangman_art import stages, logo # separate py files with ascii art to use in this file
from hangman_words import word_list

#generate word for game. Random choice from hangman_words py file
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#testing code, comment out when game is live
print(f'Pssst, the solution is {chosen_word}.')

#create blanks e.g. cat = _ _ _
display = []
for _ in range(word_length):
    display += "_"

#get user's guess
while not end_of_game:
    guess = input("Guess a letter: ").lower()

#if user already guessed letter, print statement to let them know
    if guess in display:
        print(f"You've already guessed {guess}")
    
#for loop to go through each position in word. Creates 'letter' variable for each position of chosen word e.g. 'cat' --> 'c'. Then compares this against user's guess. If matches then replaces _ e.g. 'c _ _'
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

#check if user guess is wrong, if lives run out, end the game
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. You have {lives} lives.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

#join the letters and '_' from the list [display] and turn into a string
    print(f"{' '.join(display)}")

#check if user has guessed all of the letters, i.e. no '_' remaining and then end the game
    if "_" not in display:
        end_of_game = True
        print("You win.")

#take the ascii art from the imported file and print corresponding hangman picture for each round of the game
    print(stages[lives])