print("Hello! PYTHON, Guido Van Rossum -> (1991)") # Basic Code in Python

import sys
print(sys.version) # Version

a = 20 # Assigning a Values to Variables [a = int(10) -> Casting]
b = float(20) # Type Conversion [B, b -> Case Sensitive]
str = ' Swetha Lokeshwaran ' # Assigning a String to a Variable -> ' ' quote

print(type(a)) # Check the Data Type

# Global Keyword
def myfunc():
    global str
    str = "Swetha Prabakaran" # -> " " quote
myfunc()
print("Output for Global Function:"+ str)

# Built - in Modules
import random
print(random.randrange(1,10))

# Strings:
print(str[0]) # Strings are Array

for  x in str: # Looping through a string
    print(x)

print(len(str)) # Length of a string

print("Swetha" in str) # True
print("Swetha" not in str) # False

# String Slicing
print(str[0:6]) # Start:End
print(str[:6])
print(str[2:])
print(str[-5:-2])

# Modifying Strings
print(str.upper()) # Uppercase
print(str.lower()) # Lowercase
print(str.strip()) # Remove Whitespace
print(str.replace("Swetha","Swey")) # Replacing
print(str.split(",")) # Splitting

# Concatenate
print(str+"Lokii")

# Format Strings
print(f"My Name is {str} and age is {a}") # {str} -> Placeholder