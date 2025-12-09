# JSON :
    # Syntax for storing and exchanging data
    # Text, Written with Javascript Object Notation
    # Built - in Package

# JSON to Python :

import json
x = '{"name" : "Swey", "age" : 20}'
y = json.loads(x)
print(y["age"])

# Python to JSON :

X = {
    "name" : "Swetha",
    "age" : 20
}
Y = json.dumps(X, indent=4) # Format
print(Y)

# RegEXP :
    # Sequences of characters that forms a search pattern
    # Used to check if a string contains the specified search pattern

import re
text = "The rain in spain"
a = re.search("^The.*spain$", text)
if a:
    print("YES")
else:
    print("NO")

b = re.findall("ai", text)
c = re.search(r"\s", text)
d = re.split(r"\s", text)
e = re.sub(r"\s", "9", text)
f = re.sub(r"\s", "9", text, count=2)
g = re.search(r"\b\w+", text)
print(g.span())
print(g.string)
print(g.group())

# PIP :
    # Package manager for python packages, or modules
    # Modules are python code libraries

# pip --version
# pip install camelcase
# pip uninstall camelcase
# YES
# pip list

import camelcase
c = camelcase.CamelCase()
txt = "hello"
print(c.hump(txt))