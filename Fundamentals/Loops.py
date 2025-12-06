# Looping : -> for, while

# while :
i = 1
while i < 6:
    print(i)
    i = i + 1

# for :
a = "Swetha", "Lokesh"
for x in a: # Looping from a Variable
    print(x)

for y in "Prabhu": # Without Range
    print(y)

for z in range(10): # Range
    print(z)

for l in range(0,30,2): # Start,end,step
    print(l)

for s in range(10): # With else 
    print(s)
else:
    print("Stop")

# Nested Loop in for :
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, j)