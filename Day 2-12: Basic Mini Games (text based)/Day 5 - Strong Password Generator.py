#Day - 5: Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


#Random letter generation:
letter_passwords = ""
for letter in range(1,nr_letters + 1):
  random_letters = random.choice(letters)
  letter_passwords += random_letters
#Here the letters part of the password is stored in letter_passwords

#Random number generation:
number_passwords = ""
for number in range(1,nr_numbers+1):
  random_numbers = random.choice(numbers)
  number_passwords += random_numbers
#Here the number part of the passrods is stored in number_passwords 

#Random symbol genrator:
symbol_passwords = ""
for symbol in range(1, nr_symbols + 1):
  random_symbols = random.choice(symbols)
  symbol_passwords += random_symbols
#Here the symbol part of the password is stored in symbol_passwords 

#Arranging the sequence of parts:
letter_passwords = str(letter_passwords)
number_passwords = str(number_passwords)
symbol_passwords = str(symbol_passwords)

#Create a big list of all the parts:
combined_password = letter_passwords + number_passwords + symbol_passwords
#Converting the password into a list character wise for more random generation of the password:
combined_password = list(combined_password)

#Generation of final password:
random.shuffle(combined_password)
string = ''.join(combined_password)
print(f"Our complex calculations came up with this password for you: {string}\nThe generated password is very secure and safe for personal and commercial use!")


input()
