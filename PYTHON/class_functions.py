class Student:
  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gp

  def on_honor_role(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

