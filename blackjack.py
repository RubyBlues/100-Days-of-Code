# Day 11 of 100 Days of Code: Blackjack (WIP) - First attempt. Didn't properly use functions. Will refactor/revise with functions

from blackjack_art import logo
import random
import os

def clear_screen(): 
  os.system('cls' if os.name == 'nt' else 'clear') 

begin_game = True
while begin_game:
  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_game == 'n':
    begin_game = False
  elif play_game == 'y':
    clear_screen() 
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    users_cards = random.sample(cards, 2)
    computers_cards = random.sample(cards, 2)
    users_score = sum(users_cards)
    
    # print statements for debugging
    # print(f"DEBUG: Computer's first two cards: {computers_cards}")
    
    print(f"    Your cards: {users_cards}, current score: {users_score}")
    print(f"    Computer's first card: {computers_cards[0]}")
    
    # If sum of computer's cards are less than 17, computer must select another card
    while sum(computers_cards) < 17:
      computers_cards += random.sample(cards, 1)
    computers_score = sum(computers_cards)
    # print(f"DEBUG: Computers cards after deciding if sum less than 17: {computers_cards}")
    
    take_another_card = True
    while take_another_card:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        users_cards += random.sample(cards, 1)
        users_score = sum(users_cards)
        print(f"    Your cards: {users_cards}, current score: {users_score}")
        print(f"    Computer's first card: {computers_cards[0]}")
        if 11 in users_cards and users_score > 21:
          users_cards.remove(11)
          users_cards.append(1)
          users_score = sum(users_cards)
          print("    Whoops that's more than 21, but you have an ace. Let's put it to work!")
          print(f"    Your adjusted cards are now: {users_cards}, current score: {users_score}")
        if users_score > 20:
          take_another_card = False
      if another_card == 'n':
        take_another_card = False
    
    print(f"    Your final hand: {users_cards}, final score: {users_score}")
    print(f"    Computer's final hand: {computers_cards}, final score: {computers_score}")
    
    # Deciding winner logic
    if users_score > 21:
      print("You went over, you lose 😞")
    elif users_score == computers_score:
      print("It's a draw!")
    elif users_score > computers_score or computers_score > 21:
      print("Hooray, you win! 😁")
    else:
      print("Bad luck, you lose 😞")
    


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

