# Encapsulation : 
    # Protecting data inside a class
    # __age -> private property
    # keeping data(properties) and methods together in a class, while controlling how the data can be accessed from outside the class

class Person:
  def __init__(self, name, age, salary):
    self.name = name
    self.__age = age # Private Property 
    self._salary = salary # Protected Property
  def get_age(self): # get Private Property
    return self.__age # It doesnot contain directly so far it contain as a another method
  def set_age(self, age): # set Private Property
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")
p1 = Person("Swetha", 20, 50000)
print(p1.get_age())
p1.set_age(21)
print(p1.get_age())
print(p1._salary)

# Create a Private Method :

class Calculator:
  def __init__(self):
    self.result = 0
  def __validate(self, num): # Private Method
    if not isinstance(num, (int, float)):
      return False
    return True
  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")
calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

# Name Mangling :
    # __age becomes _Person__age.