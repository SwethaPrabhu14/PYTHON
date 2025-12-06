# Tuple: -> ()
    # Used to Stores a Multiple items in a Single Variable
    # Ordered, UnChangeable, Allow Duplicate Values

tup = ("apple", "banana")
print(tup) # Tuple

print(len(tup)) # length

print(type(tup)) # type 

tup2 = tuple(("mango")) # Constructor

# Access :
print(tup[0])
print(tup[-1])
print(tup[0:1])
print(tup[1:])
print(tup[:2])
print(tup[-2:-1])

# Change the tuple of value with converts a list :

x = ("Phone", "laptops")
y = list(x)
y[0] = "computer"
y.append("boards") # append
y.remove("laptops") # remove
# del x 
x = tuple(y)
print(x)

# Unpacking a Tuple :

fruits = ("orange", "kiwi", "mango", "melon")
(a, *b, c) = fruits
print(a)
print(b)
print(c)

# Looping :

# for :
for c in fruits:
    print(c)

# while :
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# join :
mytup = fruits * 2
print(mytup)