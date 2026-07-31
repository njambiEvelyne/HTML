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

print()
#Testing multiple Conditions
print("Testing multiple conditions")
requested_topping = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_topping:
   print("Adding mushrooms.")
if "peppperoni" in requested_topping:
   print("Adding Pepperoni")
if "extra cheese" in requested_topping:
   print("Adding extra cheese")
print("\nFinish making your pizza")

print()
#Alein colors
print("Alien colors")
alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
   print("You just earned 5 points.")
if "yellow" in alien_color:
   print("You just earned 10 points.")
if "red" in alien_color:
   print("You just earned 15 points.")
print()

#Stages of life
print("The stages of life")
age2 = 3
if age2 <2:
   print("Still a child")
elif age2 ==2 or age2< 4:
   print("Still a toddler")
elif age2 ==4 or age2 <13:
   print("Still a kid")
elif age2 ==13 or age2 <20:
   print("Stll a teenager")
elif age2 ==20 or age2 <65:
   print("Person is adult")
else:
   print("The person is an elder")

print()

requested_topping2 = ["mushrooms", "extra cheese", "french fries"]
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pinapple", "extra cheese"]
for requested_toppings2 in requested_topping2: 
   if requested_toppings2 in available_toppings:
      print(f"Adding {requested_toppings2}.")
   else:
      print(f"Sorry, we do not have {requested_toppings2}.")

print("\nFinished making your pizza")   
print()
print("Username lists")
users= ["admin", "eve", "rose", "peter","elizabeth"]
for user in users:
   if user == "admin":
      print(f"Hello admin")
   else:
      print (f"Hello {user}")
print()

# current_users = ["roset", "lizbet", "rosa", "peet", "robin"]
# new_users = ["peter", "roset", "rose", "peet","elizabeth"]
# user_name = input("Enter your user name: ")

# for current_user in current_users:
#    if user_name.capitalize() == current_user.capitalize():
#       print(f"The user name {user_name} has been taken. Add a new one!")
#       #break
#    if user_name.capitalize != current_user.capitalize():
#       print("The username is available!")
#       #break
print()

ordinal_list = list(range(1,10))
print(ordinal_list)
for number in ordinal_list:
   if number == 1:
      print("1st")
   elif number ==2 :
      print("2nd")
   elif number ==3:
      print("3rd")   
   else: 
      print(f"{number}th")
print()

##DICTIONARIES
alien_0={
   "color": "green",
   "points": 5
}
print(alien_0)
print(alien_0["color"])
print("Adding key-value pairs in a dictionary")
alien_0["x-position"] =0
alien_0['y-position']= 25
print(alien_0)
print("Changing the values of a dictionary")
alien_0["color"] = "red"
print(f"The alien color is {alien_0['color']}")
alien_0["speed"]="medium"
print(alien_0)

print(f"Original x-position: {str(alien_0['x-position'])}")
#Move alien to the right
#Determine how far to move the alien based on its current speed
if alien_0["speed"]== "slow":
   x_increment = 1
elif alien_0["speed"] =="medium":
   x_increment = 2
else:
   x_increment = 3
#The new position plus the increment
alien_0["x-position"] = alien_0["x-position"] + x_increment
print(f"New postion: {str(alien_0['x-position'])}")
print()
person = {
   "firstname": "Evelyne",
   "lastname": "Njambi",
   "age": 21,
   "city": "Nakuru"
}
print(person)
for name in person:
   print(f"{person['age'], person['city'], person['firstname'], person['lastname']}")

print()

print("Looping through dictionaries")
user_0 ={
   'username': 'efermi',
   'first': 'enrico',
   'last': 'fermi'
}
for key, value in user_0.items():
   print("\nKey: " + key)
   print("Value: " + value)

print()
favourite_languages = {
   "jen":"python",
   "sarah": "c",
   "edward": "ruby",
   "phil": "python"
}
for name, language in favourite_languages.items():
   print(f"{name.title()}'s favorite language is {language.title()}.")
print()
friends = ["phil", "sarah"]
for name in favourite_languages:
   print (name.title())
   
   if name in friends:
      print(f"Hi {name.title()}, I see your favoutite language is {favourite_languages[name].title()}!")
print()
for name2 in sorted(favourite_languages):
   print(f"{name2.title()}, thank you for taking the poll.")
print()
print("Nesting dictionaries")
alien_1= {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}
aliens = [alien_1, alien_2, alien_3]
for alien in aliens:
 print(alien)

print()
aliens = []
# Make 30 green aliens.
for alien_number in range(0,30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[0:3]:
   if alien["color"]=="green":
      alien["color"]= "yellow"
      alien["speed"]= "medium"
      alien["points"]= 10
   elif alien['color'] == 'yellow':
      alien['color'] = 'red'
      alien['speed'] = 'fast'
      alien['points'] =15
for alien in aliens[0:5]:
   print(alien)
print("...")

print()
print("Store info about an ordered pizza")
pizza1 = {
   "crust": "thick",
   "toppings": ["mushrooms", "extra cheese"]
}
print(f"You ordered {pizza1['crust']}-crust pizza with the following toppings: ")
for topping in pizza1["toppings"]:
  print(f"\t {topping}")

invited_people = {
   "course": "SOEN",
   "invited_names": ["Evelyne", "Njambi", "Rose", "Mary"]
}
print(f"The invited people are from {invited_people['course']}. Below are the names: ")
for invitee3 in invited_people["invited_names"]:
   print(f"\t{invitee3}")

favorite_languages2 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name4, language2 in favorite_languages2.items():
   print(f"\n {name4.title()}'s favorite languages are:")
   for language in language2:
      print(f"\t {language.title()}")
print()
print("Dictionary in a dictionary!")
users4 = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
   },
'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
   }
}

for username, user_info in users4.items():
   print(f"\nUsername: {username}")
   full_name = user_info["first"] + " "+ user_info["last"]
   location = user_info["location"]

   print(f"\tFull name: {full_name.title()}")
   print(f"\tLocation: {location.title()}")

# foods_supply = {
#    "fast_foods": {
#       "cakes": "marble cakes",
#       "drinks":"soda",
#       "pizza":"pepperoni"
#    },
#    "fruits":{
#       "fresh": "Apples",
#       "two_days_old": "mangoes",
#       "one_week_old":"Water melon"
#    }
# }

# for food, details in foods_supply.items():
#    print(f"\n food: {food}")
#    food_detail = details["cakes"] + " " + details["pizza"]

#User input and loops
# height = input("How tall are you in inches? ")
# height = int(height)
# if height >=36:
#    print("\nYou are tall enough to ride!")
# else:
#    print("\n You will be able to ride when you become a littel bit taller!")
current_number= 0
while current_number<=5:
   print(current_number)
   current_number +=1
   
   
prompt = "\n Tell me something I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program: "
active = True
while active:
   message = input(prompt)
   if message =='quit':
      active = False
   else:
      print(message)

prompt2 = "\n Please enter the city you visited:"
prompt2 = "\n (Enter 'quit' when you are finished.)"

while True:
   city = input(prompt2)
   if city == 'quit':
      break
   else:
      print("I'd love to go to " + city.title() + "!")
print()

#Using a while loop with lists and dictionaries
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
   current_user = unconfirmed_users.pop()
   print(f"Veryfying user: {current_user.title()}")
   confirmed_users.append(current_user)
#Display all confirmed users
print("The following users have been confirmed: ")
for confirmed_user in confirmed_users:
   print(confirmed_user.title())
print()
#Removing all instances of specific values from a list
pets = ["dog", "cat", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
   pets.remove("cat")
print(pets)
print()
#Filling a Dictionary with user input
#Adding data in a dictionary
responses ={}
polling_active = True
while polling_active:
   name0 = input("\nWhat is your name? ")
   response =input("Which mountain would you like to climb someday? ")
  
   #Store responses in a dictionary
   responses[name0] = response

   #Find out if anyone else is going to take the poll
   repeat = input("Would you like to let another person respond? (yes/ no)")
   if repeat == "no":
      polling_active = False
# Polling is complete...Show results.
print("\n---Poll results---")
for name9, response in responses.items():
   print(f"{name0} would like to climb {response}.")

#Functions
def greet():
   print("Hello user")
greet()
#Return statements
def formatted_name(first_name, last_name):
   full_name = first_name + last_name
   return full_name.title()
   
musician = formatted_name("Evelyne", "Njambi")
print(musician)

#Making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
   """
   Return a full name, neatly formatted
   """
   full_name2 = first_name + ' '+ middle_name + ' '+ last_name
   return full_name2

musician2 = get_formatted_name("Eva", "Rosa", "Emilia")
print(musician2)
#Returning optional name selection
# def get_formatted_name2(first_name, middle_name, last_name):
#    if middle_name:
#       full_name = first_name + ' ' + middle_name + ' ' + last_name
#    else:
#       full_name = first_name + ' ' + last_name

#    return full_name.title()
# musician3 = get_formatted_name2("Evelyne", "Ng'ang'a")
# print(musician3)
# musician6 = get_formatted_name2("Rose", "Mary", "Muthoni")
# print(musician6)
def get_formatted_name2(first_name, last_name):
 """Return a full name, neatly formatted"""
 full_name = first_name + last_name
 return full_name.title()

while True: 
   print("\nPlease tell me our name:")
   print("(Enter 'q' at any time to quit)")
   
   f_name = input("First name:")
   if f_name == 'q':
     break 

   l_name = input("Last Name")
   if l_name == 'q': 
      break

formatted_name = get_formatted_name2(f_name, l_name)
print (formatted_name)
print()

#Passimg a list in a dictionary
def greet_user(names6):   
   """Print a simple greeting to each user in the list"""
   for name7 in names6:
      msg = "Hello ," + name7.title() + "!"
      print(msg)
user_names = ["hannah", "ty", "margot"] 
greet_user(user_names)

#Modifying a list using functions

def print_models(unprinted_models, completed_models):
   """
   Simulate printing each design until none is left.
   Move each design to completed_models after printing
   """
   while unprinted_models:
      current_design = unprinted_models.pop()
      
      #Simulate creating a 3D print from the design
      print(f"Printing model:{current_design}")
      completed_models.append(current_design)
def show_completed_models(completed_models):
   """
   Show all the models that were printed
   """
   print("\nThe following models have been printed:")
   for complete_design in completed_models:
      print(complete_design)

unprinted_models = ["i phone case", "robot pendant", "dodecahedron"]
completed_models =[]
print_models(unprinted_models, completed_models)
show_completed_models(completed_models)