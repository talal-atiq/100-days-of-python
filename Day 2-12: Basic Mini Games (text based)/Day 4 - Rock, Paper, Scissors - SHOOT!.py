#Day - 4: Rock, Paper, Scissors:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#importing the modules:
import random
#Getting the input:
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Papers or 2 for Scissors. "))

#Computer Choosing:
computer_choice = random.randint(0,2)

#Processing:
#Graphics:
if user_choice == 0:
  print("Your choice is: ")
  print(rock)
if user_choice == 1:
  print("Your choice is: ")
  print(paper)
if user_choice == 2:
  print("Your choice is: ")
  print(scissors)
  

if computer_choice == 0:
  print("The bot chose: ")
  print(rock)
if computer_choice == 1:
  print("The bot chose: ")
  print(paper)
if computer_choice == 2:
  print("The bot chose: ")
  print(scissors)

#Actual logical checking:
if user_choice == computer_choice:
  print("Both of you chose the same. Try Again")
elif user_choice == 0 and computer_choice == 2:
  print("Yaay, you WON!")
  print("No need to celebrate. I'm just a computer program created using Python.")
elif user_choice == 1 and computer_choice == 0:
  print("Yaay, you WON!")
  print("No need to celebrate. I'm just a computer program created using Python.")
elif user_choice == 2 and computer_choice == 1:
  print("Yaay, you WON!")
  print("No need to celebrate. I'm just a computer program created using Python.")
else:
  print("Dumbass, you lost to a Human made program. Look at yourself in the mirror.")
input()  
