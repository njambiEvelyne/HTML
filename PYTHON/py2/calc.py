num1 = float(input("Enter the first number: "))
operator = input("Enter the operator('+', '-', '/', '*')")
num2 = float(input("Enter the second number: "))
if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  if num1 == 0:
    result= "Error. Cannot divide by zero"
  else:
    result = num1 / num2
else:
  result = "Invalid Oprerator"

print("Result: ", result)

#Checking for odd or even numbres
num = int(input("Enter a number: "))
if num % 2 ==0:
  print("Even Number")
else:
  print("Odd Number")
