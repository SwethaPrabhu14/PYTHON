# Arrays : 
    # Don't have built-in
    # Used to store mutliple values in a one single variable

# Access :
a = ["Swetha", "lokesh"]
x = a[0]
print(x)

a[1] = "lokeshwaran" # Modifying
print(len(a)) # Length

for x in a:
    print(x)

a.append("Vishwa")
a.pop()
print(a)

# iterators :
    # An Object that contains a countable number of values
    # __iter__() and __next__()

# iterable :
tup = ("apple", "banana")
mytup = iter(tup)
print(next(mytup))
print(next(mytup))

# iterator :

for x in tup:
    print(x)