print("""
 _   _                 _                 _____                     _             
| \ | |               | |               |  __ \                   (_)            
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` |
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |
                                                                            __/ |
                                                                           |___/ 
""")
numbers = list(range(1,101))
import random
guess =  random.choice(numbers)
#print(f"The guessed number is {guess}") For testing purposes only
exit_game = False
while not exit_game:
  level = input("Which level you wanna play on?\nType 'h' for hard and 'e' for easy\n")
  number_of_attempts = 0
  if level == "h" or level == "H" or level == "Hard" or level == "hard":
    number_of_attempts += 5
    print(f"You now have a total of {number_of_attempts} attempts to guess the number.\nGood Luck :)\n")
  else:
    number_of_attempts += 10
    print(f"You now have a total of {number_of_attempts} attempts to guess the number.\nGood Luck :)\n")
  exit = False
  while not exit:
    if number_of_attempts > 0:
      user = int(input("Your guess: "))
      no = guess - user
      if no == 0:
        number_of_attempts -= 1
        print(f"Hoorah, you guessed the number just right with {number_of_attempts} attempts left.\n")
        exit = True
        again = input("You wanna play again (Y/N):  ")
        if again == "Y":
          exit_game = False
        else:
          exit_game = True
          print("Bye!")
      elif no <= 5 and no >= -5:
        number_of_attempts -= 1
        print(f"Close! But still not there yet! You now have {number_of_attempts} attempts remaining.\nGuess again.\n")
        exit = False
      elif no < -5:
        number_of_attempts -= 1
        print(f"That's just 'TOO HIGH'. You now have {number_of_attempts} attempts left.\nGuess again.\n")
        exit = False
      elif no > 5:
        number_of_attempts -= 1
        print(f"That's just 'TOO LOW'. You now have {number_of_attempts} attempts left.\nGuess again.\n")
        exit = False
    else:
      print("Oops, looks like have zero attempts left. You Lost!\n")
      print(f"The guessed number was {guess}.")
      exit = True
      again = input("You wanna play again (Y/N):  ")
      if again == "Y":
          exit_game = False
      else:
          exit_game = True
          print("Bye!")

  input()    
