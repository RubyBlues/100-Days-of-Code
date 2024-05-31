#Day 4 of 100 Days of Code: Make a rock, paper scissors game against the computer

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = input("What do you choose? Rock, Paper or Scissors?\n").lower()
if choice == "rock":
  print(f"You chose:\n {rock}")
if choice == "paper":
  print(f"You chose:\n {paper}")
if choice == "scissors":
  print(f"You chose:\n {scissors}")
else:
  print(f"There are only 3 options in 'Rock, Paper, Scissors'. {choice} is not one of them.'")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
if computer_choice == "rock":
  print(f"Computer chose:\n {rock}")
if computer_choice == "paper":
  print(f"Computer chose:\n {paper}")
if computer_choice == "scissors":
  print(f"Computer chose:\n {scissors}")
  

if choice == computer_choice:
  print("It's a draw!")
elif choice == "rock" and computer_choice == "scissors":
  print("You win!")
elif choice == "scissors" and computer_choice == "paper":
  print("You win!")
elif choice == "paper" and computer_choice == "rock":
  print("You win!")
else:
  print("You lose!")
