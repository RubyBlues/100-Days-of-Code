#Day 3 of 100 Days of Code: Leap Year Calculator

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if (year % 4 == 0):
  if (year % 100 != 0):
    print("Leap year")
  elif (year % 400 == 0):
    print("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year")