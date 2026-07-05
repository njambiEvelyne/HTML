names = ["Evelyne", "Njambi", "Peter", "Rosemary", "Victor"]
mode_of_transportation = ["Road", "Air", "Railway", "Water"]
names.append("Elizabeth")
names.insert(0, "Peter")
deleted_items = names.pop()
print(deleted_items)

for name in names:
  for mode in mode_of_transportation:
      print(f"Hello {name}. You love using {mode} for travelling.")
  print()

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

invitees = ["Rose", "Roselyne", "Maish", "harry"]
for invitee in invitees:
   print(f"Hello {invitee}. You are invited to this special dinner! Welcome")

print()

#not_attending = invitees.pop(0)
#print(f"{not_attending} will not br attending the dinner")
new_attendee = invitees.insert(0, "Harrington")
for attendees in invitees:
   print(f"{attendees} will be attending the dinner!")

print()
for attendee in invitees:
   print(f"{attendee.title()}. We are pleased to inform you that we have found a bigger dinning table!")

print()
names2 = ["Evelyne", "Rosemary","Njambi", "Peter",  "Victor"]
names2.sort()
print(names2)
print(f"The lenght for the list is: {len(names2)}")
print()

#Pizza stores
pizza = ["Pepperoni", "Margheritta", "Supreme Pizza"]
for pizz in pizza:
   print(f"I love {pizz} pizza")
print("I really love pizza!")
print()

numbers = list(range(1,6))
print(numbers)
print()
print("Even numbers")
even_numbers = list(range(0,11,2))
print(even_numbers)
print()

squares = []
for value in range(1,10):
   square = value **2
   squares.append(square)
print(squares)
print()

print("Results from a list comprehension:")
squares2 = [value **2 for value in range(1,13)]
print(squares2)
print()
for num in range(1,21):
   print(num)
print()

print("A list of all odd numbers")
for number2 in range(1,21):

   if number2 %2 !=0:
      print(number2)

cube = [values **3 for values in range(1,20)]
print(cube)
print()

my_foods = ["Pizza", "falafel", "carrot cake"]
friends_food = my_foods[:]
print(friends_food)
my_foods.append("cannoli")
print(my_foods)

#Tuples
# dimensions = (20, 40)
# print("Original Dimensions:")
# for dimension in dimensions:
#    print(dimensions)

# dimensions = (400, 100)
# print("Modified dimensions")
# for dimemsion in dimensions:
#    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
  print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
 print()

#Buffet
print("List of foods offered: ")
foods = ["Orange Chicken", "Pizza", "Mashed Potato", "Grilled chicken", "Chapati"]      
for food in foods:
   print (food)
print()

print("Revised menu")
foods = ["Orange Chicken1", "Pizza2", "Mashed Potato3", "Grilled chicken4", "Chapati5"]
for food in foods:
   print (food)

print()
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
   print(f"{user.title()} you can post a response you wish.")
   
age = 12
# if age <4:
#    print("Your admission cost is $0.")
# elif age <18:
#    print("Your admission cost is $5.")
# else:
#    print("Your admission cost is $10.")
if age < 4:
   price =0
elif age <18:
   price = 5
elif age <65:
   price = 10
else:
   price = 5


#Testing multiple Conditions
requested_topping = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_topping:
   print("Adding mushrooms.")
if "peppperoni" in requested_topping:
   print("Adding Pepperoni")
if "extra cheese" in requested_topping:
   print("Adding extra cheese")
print("\nFinish making your pizza")

