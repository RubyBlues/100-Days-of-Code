# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

coin_flip = random.randint(0, 1)

if coin_flip == 0:
  print("Tails")
if coin_flip == 1:
  print("Heads")