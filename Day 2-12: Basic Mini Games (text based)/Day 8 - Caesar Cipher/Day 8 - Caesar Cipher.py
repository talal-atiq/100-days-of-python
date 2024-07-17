import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '*', '/', '=', '-', '_']

print(art.logo)

def cipher(plain_text, shift_position, choice):
  cipher = ""
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      if choice == "encode":
        new = alphabet[position + shift_position]
        cipher += new
      if choice == "decode":
        new = alphabet[position - shift_position]
        cipher += new
    elif char in numbers:
      position = numbers.index(char)
      if choice == "encode":
        new = numbers[position + shift_position]
        cipher += new
      if choice == "decode":
        new = numbers[position - shift_position]
        cipher += new
    elif char in symbols:
      position = symbols.index(char)
      if choice == "encode":
        new = symbols[position + shift_position]
        cipher += new
      if choice == "decode":
        new = symbols[position - shift_position]
        cipher += new    
      
    else:
      cipher += char 
  print(f"Your {choice}d text will be {cipher}.")  

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25:
    shift = shift % 26  
  
  cipher(plain_text = text, shift_position = shift, choice = direction)
  check = input("Type 'Y' if you want to continue and 'N' to exit.\n")
  if check == "n" or check == "N":
    should_continue = False
    print("Good Bye! It was a pleasure having you.\nSee you again next time. :)")

input()    

  

