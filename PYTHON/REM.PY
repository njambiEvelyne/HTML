# # function
# def sayhi():
#   name = input("Enter your name: ")
#   print(f"Hello {name}")

# sayhi()

# def cube_number():
#   num = int(input("Enter the number:"))
#   result= num*num*num
#   print(result)
#   return(result)
  
# cube_number()

# #if Statements
# is_female = True
# is_tall = True
# if(is_female or is_tall):
#   print("You are a lady or tall or both")

# elif(is_female and not is_tall):
#   print("You are a short female")

# elif not(is_female) and is_tall:
#   print("You aer not a female but are tall")

# else:
#   print("You are neither female nor tall")

# #If satatements and comparison statements
# def max_num(num3, num4, num5):
#   if num3 >= num4 and num3 >=num5:
#     return num3
  
#   elif num4>= num3 and num4 >= num5:
#     return num3
  
#   else:
#     return num5
  
# print(max_num(3,5,6))
   

#Dictionaries
month_conversions = {
  "Jan": "January",
  "Feb":"February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sept": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
}
print(month_conversions.get("Luv", "Not a valid Key"))

i=1 
while (i<=9):
  print(i)
  i+=1

print("Done with loop")

#For loop
friends=["Jane", "Karen", "Kevin"]
for friend in friends:
  print(friend)

for num in range((len(friends))
)  :
  print(num)

for index in range(10):
  print(index)

for ind in range(5)
  if ind == 0:
    if i== 0:
      print("First Iteration")
    else:
      print("Not first")

def raise_to_power(base_number, pow_num):
   result4 = 1
   for index2 in range(pow_num):
     result4 = result4 * base_number
   return result4

print(raise_to_power(2,4))

number_grid = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]
print(number_grid[2] [1])

for row in number_grid:
  for column in row:
    print(column)
    




  



