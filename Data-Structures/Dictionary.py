# Dictionary: -> {key : value}
    # Used to Stores a Multiple items in a Single Variable
    # Ordered*, Changeable, and do not Allow Duplicate Values

dict1 = {"name" : "Swetha", "age" : 20, "location" : "Panruti"}
print(dict1) # dictionary

print(len(dict1)) # length

print(type(dict1)) # Type

dict2 = dict(name = "lokesh", age = 20, location = "Panruti") # Constructor

# Access :

print(dict1["name"])
print(dict1.get("age"))
print(dict1.keys())
print(dict1.values())
dict1["regno"] = 153
print(dict1)

# Changing a Value

dict2["name"] = "Lokeshwaran"
dict2.update({"regno" : 1468})
# dict2.pop("name")
# dict2.popitem()
# del dict2["age"]
# del dict2
# dict2.clear()

# Looping :

for x in dict1:
    print(x) # keys
    print(dict1[x]) # Values

for y in dict1.values():
    print(y)

for i, j in dict1.items():
    print(i, j)

# Methods :

dict3 = dict1.copy()
print(dict3)

# Nested dictionary :

dict4 = {
    "sweyy" : {
        "age" : 20
    },
    "lokii" : {
        "age" : 21
    }
}