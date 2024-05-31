# Day 5 of 100 Days of Code: Average Height
# Auditorium server is down so adapting code from video to work on in replit
# Auditorium starter code:
''' student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
'''

student_heights = [151, 145, 179]
heights_sum = 0

for i in student_heights:
  heights_sum += i

number_of_students = 0
for i in student_heights:
  number_of_students += 1

average_student_height = heights_sum / number_of_students
average_student_height = round(average_student_height, 2)

print(f"The average height of a student is {average_student_height}cm.")