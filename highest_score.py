# Day 5 of 100 Days of Code: Highest Score
# High Score: You are going to write a program that calculates the highest score from a list of scores. Not allowed to use the min/max functions
# Use Auditorium starter code 
student_scores = input("Please enter some student scores without commas").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write own code below here:

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}.")
  