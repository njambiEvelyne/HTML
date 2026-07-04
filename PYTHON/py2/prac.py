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

invitees = ["Rose", "Roselyne", "Maish", "Harry"]
for invitee in invitees:
   print(f"Hello {invitee}. You are invited to this special dinner! Welcome")

print()

#not_attending = invitees.pop(0)
#print(f"{not_attending} will not br attending the dinner")
new_attendee = invitees.insert(0, "Harrington")
for attendees in invitees:
   print(f"{attendees} will be attending the dinner!")



