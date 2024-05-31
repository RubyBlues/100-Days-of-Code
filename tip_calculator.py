#Day 2 of 100 Days of Code: Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))


tip_reworked = 1 + (tip/100)
bill_with_tip = total_bill * tip_reworked
amount_to_pay = bill_with_tip / number_of_people

amount_to_pay = round(amount_to_pay, 2)
#  to give 2dp to represent currency, use the following
amount_to_pay = "{:.2f}".format(amount_to_pay)

print(f"Each person should pay: ${amount_to_pay}")