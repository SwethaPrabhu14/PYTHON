# Classes-Objects :
    # An class defines what an object should look like, and an object is created based on that class.
    # A class is like an object constructor, or an "Blueprint" for creating objects.

# class  : -> Fruit
# Object : -> Apple, Banana

# Advantages :

    # Provides a clear structure to programs
    # Makes code easier to maintain, reuse and debug
    # Helps keep your code DRY(Don't Repeat Yourself)
    # Allows you to build reusable applications with less code

# Creating a class :

# SYNTAX :
# class classname:
#     code

class person:
    pass

# Creating a Object :

# SYNTAX :
# objectname = classname()
# objectname.classname()

# p1 = person("Swetha")
# p1.person()

# __init__() method :
    # When the class is being initiated.

class myperson:
    spl = "Lokesh" # Class Property
    def __init__(self, name, age = 21): # Default Values -> age = 21 : Self parameters
        self.name = name # Object / Instance Property
        self.age = age
    def greet(self): # Class Methods -> By using self keyword to accessing all the functions
        print("Hello, "+ self.name) 
a1 = myperson("Swey", 20)
a1.greet()
print(a1.name)
print(a1.age)
print(a1.spl)

# Inner Classes :

# Creating a inner class
class Outer:
  def __init__(self):
    self.name = "Outer Class"
  class Inner:
    def __init__(self, outer):
      self.outer = outer
      self.name = "Inner Class" # Accessing outer class from inner class
    def display(self):
      print("Hello, Inner class")
      print(f"Outer class name: {self.outer.name}")
outer = Outer()
inner = outer.Inner(outer) # Accessing inner class from outside
inner.display()
print(outer.name)