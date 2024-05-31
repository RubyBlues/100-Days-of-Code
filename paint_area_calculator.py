# Day 8 of 100 Days of Code: Paint Area Calculator

# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  number_of_cans = (test_h * test_w) / cover
  roundup_cans = math.ceil(number_of_cans)
  print(f"You'll need {roundup_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Please enter the height of the wall")) # Height of wall (m)
test_w = int(input("Please enter the width of the wall")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
