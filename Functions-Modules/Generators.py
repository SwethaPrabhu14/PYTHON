# Generators : 
    # Can Pause and resume
    # Return -> Yield

def mygenerator():
    yield 1
    yield 2
    yield 3
for value in mygenerator():
    print(value)

# List comprehension :
list1 = [x * x for x in range(5)]
print(list1)

# Generators Expression : 
genexp = (x * x for x in range(5))
print(genexp)
print(list(genexp))

# Generators Methods :

def echo_gen():
    while True:
        received = yield
        print("Received : ", received)
gen = echo_gen()
next(gen)
gen.send("Hello") # send()

def func():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Closed")
a = func()
print(next(a))
a.close() # close()