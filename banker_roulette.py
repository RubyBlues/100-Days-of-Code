#Day 4 of 100 Days of Code: Banker Roulette
# names = names_string.split(", ") -- edited for saving here as original file on Auditorium had pre-populated input
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
number_of_names = len(names)
random_index = random.randint(0, number_of_names - 1)
random_name = names[random_index]

print(f"{random_name} is going to buy the meal today!")