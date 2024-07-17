from replit import clear
import art
print(auctionlogo.logo)
print("Welcome to our auction program\nIt's nice having you here\nDo note that, this is a silent auction and all the bids shall be kept private.")
bids = {
}
biding_exit = False
while not biding_exit:
  name = str(input("Enter your name: \n"))
  bid_price = int(input("How much money you wanna bid: \n$"))
  bids[name] = bid_price
  check = input("Anymore bidders. (Y/N):\n")
  if check == "Y" or check == "y":
    clear()
  else:
    biding_exit = True
    set_amount = 0
    set_person = ""
    for price in bids:
      if bids[price] > set_amount:
        set_amount = bids[price]

    for winner in bids:
      if bids[winner] == set_amount:
        win = winner

    print(f"The auction has ended.\nAnd we have the winner.\n-*drum rolls*-\nThe winner is {win} with a {set_amount}$ bid.\nCongrats!")    
        

    



