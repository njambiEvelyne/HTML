print("Welcome to The Calculator Application")
instructions = {
  1: "Addition",
  2: "Subtarction",
  3: "Mulitplication",
  4: "Division",
  5: "Modulus"

}
# print(instructions)
choice = int(input(f"Make your slection based on the given instructions above{instructions}"))

def add():
  print("This is addition")
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = num1 + num2
  print(result)

def subtract():
  print("This is subtraction")
  num1 = int(input("Enetr the first number: "))
  num2 = int(input("Enter the second number: "))
  if(num2 > num1):
    print("The result is negative")
    result = num1 - num2
  else:
    print("The result is positive")
    result = num1-num2

def multiply():
  print("This is multiplication")
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = num1 * num2
  print(result)

def divide():
  print("This is division")
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  if(num2 ==0):
    print("Zero didvision error")
  else:
    result = num1 /num2
    print(result)

def modulus():
  print("This is modulus")
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = num1 %num2
  print(result)
