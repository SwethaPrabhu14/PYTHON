# Decorators :
    # Add extra behavior to a function, without changing the function code
    # Function that takes another function as input and returns a new function

def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase # Decorators 
def myfunction():
    return "Hello"
print(myfunction())

def a():
    return "Swetha"
print(a.__name__) # Identifying the function name

# @functools.wraps -> original function name and docstring

# lambda :
    # Small anonymous function
    # Take any number of arguments, but can only have a 1 expression
# Syntax :
    # lambda arguments : expression

x = lambda a : a + 10
print(x(5)) 

# Map 
num = [2, 4, 6, 8, 12]
a = list(map(lambda x : x * 2, num))
print(a)

# filter
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(filter(lambda x : x % 2 != 0, number))
print(a)