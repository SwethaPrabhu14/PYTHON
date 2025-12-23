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