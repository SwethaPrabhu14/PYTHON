# Set: -> {}
    # Used to Stores a Multiple items in a Single Variable
    # UnOrdered, UnChangeable, do not Allow Duplicate Values and UnIndexed

set1 = {"apple", "banana", "orange"}
print(set1) # Set

print(len(set1)) # length

print(type(set1)) # Type

set2 = set(("kiwi", "pineapple")) # Constructor

# Access :

for x in set1:
    print(x)

print("banana" in set1)

# Methods :

set1.add("mango")
set1.update(set2)
set1.remove("orange")
set2.discard("pineapple")
# set1.pop()
# set1.clear()
# del set1

# Looping for :

for x in set1:
    print(x)

# Join :
    # Union -> |
    # Intersection -> &
    # difference -> -
    # set difference -> ^

a = {"Phone", "laptops", "Computers"}
b = {"laptops", "boards", "RAM"}
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
a.intersection_update(b)
a.difference_update(b)
a.symmetric_difference_update(b)

# Frozenset :
    # Immutable version of a set
    # Contains Unique, Unordered, and Unchangeable
    # Cannot be added and removed
    # frozenset()

x = frozenset({"bike", "cars", "lorry"})
y = frozenset({"auto"})
print(x)

# Methods :

x.copy()
x.union(y)
x.intersection(y)
x.difference(y)
x.symmetric_difference(y)