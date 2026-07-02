# import usefull_tools
# print (usefull_tools.beatles)
# print(usefull_tools.roll_dice(10))  

# CLASSES AND OBJECTS
class student:
  def __init__(self, name,major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa= gpa
    self.is_on_probation = is_on_probation

student1 = student("Evelyne", "SOEN", 12.90, False)
#print(student1.gpa)

question_prompt=[
  "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange \n\n",
  "What color are Bananas?\n(a) Teal\n(b)Magenta\n(c) Yellow\n\n",
  "What color are starwberries?\n(a) Yellow\n(b) Red\n(c)Blue\n\n"
]