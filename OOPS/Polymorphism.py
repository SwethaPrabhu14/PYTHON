# Polymorphism :
    # Many Forms
    # Different classes with the same methods
    # Can Inheritance class polymorphism

class person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def persons(self):
    print("Swetha is here!")
class person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def persons(self):
    print("Lokesh is here!")
class person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def persons(self):
    print("SweyLoki combined!")
rollno1 = person1("Swetha", "20")
rollno2 = person2("Lokesh", "20")
rollno3 = person3("SwethaLokeshwaran", "1468")
for x in (rollno1, rollno2, rollno3):
  x.persons()