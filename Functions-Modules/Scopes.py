# Local -> Inside(Access Only Within the Function)
# Global -> Outside(Access Anywhere)

# Local Scope :

def myfunc1():
    x = 300
    print(x)
myfunc1()

# Global Scope :

x = 50
def myfunc2():
    print(x)
myfunc2()
print(x)

# Combine Both Scopes :

x = 300 # Global Scope
def myfunc3():
    x = 200 # Local Scope
    print(x)
myfunc3()
print(x)

# Global Keyword : 

def myfunc4():
    global x # Local But Acts as a Global(Keyword)
    x = 456
myfunc4()
print(x)

x = 300 # Global Scope
def myfunc5():
    global x
    x = 200 # Global (Updated Value)
myfunc5()
print(x)

# Non - Local Keyword :

def myfunc6():
    x = "abc" # Local
    def myfun():
        nonlocal x # Keyword
        x = "xyz" # Local (Updated value)
    myfun()
    return x
print(myfunc6())

# LEBG Rule :
    # Local Enclosing Global Built-in