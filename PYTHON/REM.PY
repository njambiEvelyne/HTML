# function
def sayhi():
  name = input("Enter your name: ")
  print(f"Hello {name}")

sayhi()

def cube_number():
  num = int(input("Enter the number:"))
  result= num*num*num
  print(result)
  return(result)
  
cube_number()

#if Statements
is_female = True
is_tall = True
if(is_female or is_tall):
  print("You are a lady or tall or both")

else:
  print("You are neither female nor tall")



