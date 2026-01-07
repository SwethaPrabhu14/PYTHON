# Inheritance : 
    # Allows us to define a class that inherits all the methods and Properties from another class.
    
# Parent Class : Being Inherited from base class
# Child Class : Inherits from another class, derived class

class Person: # Parent Class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person): # Child Class
  pass
x = Student("Swetha", "Lokeshwaran")
x.printname()

# If Parent class has __init__() inherits that the child class also has __init__() its may occurs Overrides.

# USE :
# 1. parent_class_name.__init__()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Swetha", "Lokeshwaran")
x.printname()

# super().__init()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2026 # Add Property
  def welcome(self): # Add Methods
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Swetha", "Lokeshwaran")
x.printname()
print(x.graduationyear)
x.welcome()