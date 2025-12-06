# List : -> []
    # Used to Stores a Multiple items in a Single Variable
    # Ordered, Changeable, Allow Duplicate Values
    # Indexed
    # Contains different data types

a = ["apple", "banana"]
print(a) # list

print(len(a)) # length of the list

print(type(a)) # type

b = list(("pineapple", "grapes")) # Constructor

print(a[0]) # Access
print(a[-1]) # Negative Indexing 

print("Range of Indexes : ")
print(a[2:5])
print(a[2:])
print(a[:5])
print(a[-4:-1])

# Changing the Values with index :
b[0] = "watermelon"
print(b)

a.insert(2, "orange") # Insert
a.append("mango") # Append -> Only 1 added
a.remove("banana") # Remove
a.pop() # Removes -1 of the value
del a[0] # delete the 1st item
# del a # Entirely delete
# a.clear() #clear

# Extend -> Many of values added :
b.extend(a)
print(b)

# Looping for and while :
for x in a:
    print(x)

i = 1
while i < len(a):
    print(a[i])
    i = i + 1

# List Comprehension :
# Syntax : newlist = [expression for item in iterable if condition == True]
[print(x) for x in a] 

# Methods :

list = ["computer", "phones", "apple", "laptops"]
list.sort() 
print(list)
list.sort(reverse=True)
print(list)
list2 = list.copy()
print(list2)