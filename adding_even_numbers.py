# Day 5 of 100 Days of Code: Adding even numbers
# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100.

target = int(input("Please enter a number between 0 and 1000\n"))

even_total = 0 #accumulator
for number in range(2, target+1, 2):
  even_total += number

print(even_total)