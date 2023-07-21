from replit import clear
from art import logo
print(logo)


def add(n1, n2):
  return n1+n2

def substract(n1, n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2
  
 
input("Welcome to Calculator!")
operators = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
} 

def calculator():
  
  num1 = float(input("What is the first number? :"))
  for symbol in operators:
    print(symbol)
  
  calculation_finished = False
  
  while not calculation_finished:
    operation_symbol = input("Pick an operator: ")
    num2 = float(input("What is the second number?:"))
    calculation_function = operators[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
    if should_continue == "y":
      num1 = answer
      
    elif should_continue == "n":
      clear()
      calculator()

calculator()
      
      

