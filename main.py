from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

def max_bid(bidders):
  max_bid = 0
  winner = ""
  for bidder in bidders:
    if bidders[bidder] > max_bid:
      max_bid = bidders[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of $ {max_bid}")

continue_bidding = False
while not continue_bidding:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders = {}
  bidders[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "yes":
    clear()
  elif other_bidders == "no":
    continue_bidding = True
    max_bid(bidders)
    


  


          