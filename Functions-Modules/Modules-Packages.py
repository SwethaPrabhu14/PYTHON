# Modules & Packages :
    # numpy
    # pandas
    # scipy
    # django

# def greetings(name):
#     print("Hello" + name) # Functions.py

import Functions
Functions.greeting("Swetha") # Importing the module

a = Functions.person1["age"]
print(a) # dict

import Functions as fun # Renaming the file

# Built - in Modules :

import platform
x = platform.system()
print(x)

x = dir(platform)
print(x)

# Import from module :

from Functions import person1
print(person1["age"])

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(datetime.datetime(2025, 4, 1))
print(x.strftime("%B"))

# Math Modules :
    # min(), max(), abs(), pow(), pi

import math
x = math.sqrt(64)
y = math.ceil(1.4)
z = math.floor(1.4)
K = math.pi

print(x, y, z, K)