import sys

def add(x,y):
  return x + y

def minus(x,y):
  return x - y

def multiply(x , y):
  return x * y

def divide(x, y):
  return x / y



allowed_symbols = ['+', '-', '*', '/', 'x']

while True:
  
  operation = input("input operation to make with numbers: +, -, *, /. or x to exit:")
  if operation == 'x':
      print("Exit")
      sys.exit(1)

  else:
    if not operation in allowed_symbols:
      print("not allowed operation")
    
      
    elif operation in allowed_symbols:
      try:
        x = eval(input("first number: "))
        y = eval(input("second number: "))
        
        if operation == '+':
          print(add(x,y))
        elif operation == '-':
          print(minus(x,y))
        elif operation == '*':
          print(multiply(x,y))
        elif operation == "/":
          print(divide(x,y))
      except NameError:
        print("Input only numbers")