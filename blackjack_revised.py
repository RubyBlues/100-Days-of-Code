# Day 11 of 100 Days of Code: Blackjack. Revised attempt using functions better

from blackjack_art import logo
import random
import os

##### Functions #####
def clear_screen(): 
  os.system('cls' if os.name == 'nt' else 'clear') 

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take the player's card list and returns the score sum, i.e. [2, 10] = 12"""
  # setting rules for 'BlackJack' i.e. getting 12 with an Ace and a 10 with 2 cards
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # automatically replacing Ace = 11 with Ace = 1, if score is greater than 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    # print("    Whoops that's more than 21, but you have an ace. Let's put it to work!")
    # print(f"    Your adjusted cards are now: {users_cards}, current score: {users_score}")
  return sum(cards)

def compare(users_score, computers_score):
  # Deciding winner logic
  if users_score > 21:
    return("You went over, you lose 😞")
  elif users_score == computers_score:
    return("It's a draw!")
  elif computers_score == 0:
    return("Computer has Blackjack, sorry you lose 😞")
  elif users_score == 0:
    return("Yay, you have Blackjack. You win! 😁")
  elif users_score > computers_score or computers_score > 21:
    return("Hooray, you win! 😁")
  else:
    return("Bad luck, you lose 😞")

def play_game():
  print(logo)

  users_cards = []
  computers_cards = []
  is_game_over = False
  
  for _ in range(2):
    users_cards.append(deal_card())
    computers_cards.append(deal_card())
  
  while not is_game_over:
    users_score = calculate_score(users_cards)
    computers_score = calculate_score(computers_cards)
    print(f"    Your cards: {users_cards}, current score: {users_score}")
    print(f"    Computer's first card: {computers_cards[0]}")
    
    if users_score == 0 or computers_score == 0 or users_score > 21:
      is_game_over = True
    else:
      choose_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if choose_another_card == 'y':
        users_cards.append(deal_card())
      else:
        is_game_over = True

  # Rules: If sum of computer's cards are less than 17, computer must select another card
  while computers_score != 0 and computers_score < 17:
    computers_cards.append(deal_card())
    computers_score = calculate_score(computers_cards)

  print(f"    Your final hand: {users_cards}, final score: {users_score}")
  print(f"    Computer's final hand: {computers_cards}, final score: {computers_score}")
  print(compare(users_score, computers_score))


##### End of Functions #####

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear_screen() 
  play_game()


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

