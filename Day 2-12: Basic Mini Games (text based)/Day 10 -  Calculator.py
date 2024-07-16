#Operational Functions:
#Addition:
def add(n1, n2):
  return n1 + n2
#Subtraction:
def subtract(n1, n2):
  return n1 - n2
#Multiplication:
def multiply(n1, n2):
  return n1 * n2
#Division:
def divide(n1, n2):
  return n1 / n2

#Creating Dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculation():
  print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
  num1 = float(input("Enter the first number: \n"))
  for operands in operations:
    print(operands)
  exit_condition = False
  while not exit_condition:
    operation_symbol = input("Pick an operation from the choices above:\n")
    num2 = float(input("Enter the next number: \n"))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    check = input("Type 'Y' if you want to continue working on the same result.\n'N' to continue with a new calculation or 'E' to exit.\n")
    if check == "y" or check == "Y":
      num1 = answer
      exit_condition = False
    else:
      exit_condition = True
      calculation()
    
calculation()
input()
  
  
  
