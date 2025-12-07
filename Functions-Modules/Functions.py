# Functions :
# A block of code which only runs when it is called
# Return data as a result
# Helps avoiding code repetition
# def keyword, followed by a function name and parentheses

def myfunc(): # Function definition
    print("Hello")
myfunc() # Calling a Function

# Function Names :
    # Must start with a letter or underscore
    # Can only contain letters, numbers, and underscore
    # Case-sensitive

# Return :

def return_val():
    return "Swetha" # Return Values
msg = return_val()
print(msg)
print(return_val())

# Parameters and Arguments :

def a(name, /): # Positional Arguments -> /
    print(name)
a("Swey")

# name -> Variables(Parameters)
# Swey -> Values(Arguments)

def b(name = "Lokesh"): # Default Parameter Value
    pass
b()

def c(*, name, age): # Keyword Arguments -> *
    print("Hey " + name)
c(name = "Swethaa", age = 20)

# Dictionary :
def d(person):
    print("Name : ", person["name"])
a1 = {"name" : "swee"}
d(a1)

# *args and **kwargs :
# *args -> Arbitary arguments

def e(*names):
    print("Name is : " + names[2])
e("swetha", "lokesh", "vishwa")

# **kwargs -> Arbitary keywords arguments

def f(**kids):
    print("Name is : " + kids["name"])
f(name = "Swethaaa")

# Recursion :
    # A function calls itself

def count(n):
    if  n <= 0:
        pass
    else:
        print(n)
        count(n - 1)
count(5)

# Recursion Limit : 

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())