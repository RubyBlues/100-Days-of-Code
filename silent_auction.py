# Day 9 of 100 Days of Code: Silent Auction

from silent_auction_art import logo
# from replit import clear #HINT: You can call clear() to clear the output in the console. Works in replit, unsure of equivalent here so commented out

print(logo)

print("Welcome to the silent auction")

add_bidder = True

bidders = {}
while add_bidder:
  name = input("Please enter your name: ")
  bid = int(input("Please enter your bid amount: £"))
  bidders.update({name: bid}) # or could write bidders[name] = bid
  # print(bidders)
    
  other_bidders = input("Are there any other bidders. Type 'yes' or 'no': ").lower()
#   clear()
  if other_bidders == "no":
    add_bidder = False

number_of_bidders = len(bidders)
print(f"Thank you. We have received a total of {number_of_bidders} bidders in this auction.")

def find_highest_bidder(bidders):
  highest_bidder = max(bidders, key=bidders.get)
  print(f"The highest bidder is {highest_bidder}!")

find_highest_bidder(bidders)

