print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

score1 = t + r + u + e

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e1 = name1.count("e") + name2.count("e")

score2 = l + o + v + e1

total_string_score = str(score1) + str(score2)
total_score = int(total_string_score)

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_string_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_string_score}, you are alright together.")
else:
  print(f"Your score is {total_string_score}.")