# Inheritance helps with reusing instance variables and instance methods

class Parent():
  def __init__(self, last_name,eye_color):
    print("Parent Constructor Called")
    self.last_name = last_name
    self.eye_color = eye_color

  def show_info(self):
    print("Last Name: "+self.last_name)
    print("Eye Color: "+self.eye_color)

#Inherits from class Parent
class Child(Parent):
  def __init__(self, last_name,eye_color, number_of_toys):
    print("Child Constructor Called")
    Parent.__init__(self, last_name,eye_color)
    self.number_of_toys = number_of_toys

  #resultes in method overriding
  def show_info(self):
    print("Last Name: "+self.last_name)
    print("Eye Color: "+self.eye_color)
    print("Number of Toys: "+str(self.number_of_toys))

#Note: Keep class definition seperate from instance creation as much as possible, together here for demonstration of inheritance
tom_smith = Parent("Smith", "Green")
#tom_smith.show_info()

dick_smith = Child("Smith", "Green", 3)
#dick_smith.show_info()