# Day 2: Tip Calculator
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percent_tip = input("What percentage of tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
bill = float(bill)
percent_tip = float(percent_tip)
percent_tip = percent_tip / 100
percent_tip += 1
people = int(people)
pay = (bill/people) * percent_tip
pay = round(pay,2)
print(f"Each person should pay: {pay}$")
input()
