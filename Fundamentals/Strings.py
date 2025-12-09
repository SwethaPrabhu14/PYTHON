# Strings:

str = " Swetha "
age = 20

print("Index Value of : ",str[4]) # Strings are Array

for  x in str: # Looping through a string
    print("Looping : ",x)

print(len(str)) # Length of a string

print("Swetha" in str) # True
print("Swetha" not in str) # False

# String Slicing
print("String Slicing : ")
print(str[0:6]) # Start:End
print(str[:6])
print(str[2:])
print(str[-5:-2])

# Modifying Strings
print("Pre-defined Strings Methods : ")
print(str.upper()) # Uppercase
print(str.lower()) # Lowercase
print(str.strip()) # Remove Whitespace
print(str.replace("Swetha","Swey")) # Replacing
print(str.split(",")) # Splitting

# Concatenate
print("Concatenation of : ",str+"Lokesh")

# Format Strings
print(f"My Name is {str} and age is {age}") # {str} -> Placeholder, : -> Modifiers

# Instance
print(isinstance(age,int)) # True

# None :

x = None
print(x)
print(type(x))
print(bool(None))