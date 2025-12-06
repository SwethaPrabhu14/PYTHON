# Conditional Statements : 
# if
# elif
# else

a = 56
b = 23
c = 14
if a > b :
    print("a is large")
elif a < b :
    print("b is large")
else:
    print("default")

# Shorthand :

print("Yes") if a > b else print("No")

# Conditional Statements with logical operators :

if a > b and a < c:
    print(a)
elif b > a or b < c:
    print(b)
else:
    print(not(a == b))

# Statements :
# break
# continue
# pass

for i in range(1, 10):
    if i == 2:
        break
    print(i)

for j in range(1, 10):
    if j == 5:
        continue
    print(j)

for k in range(1, 10):
    if k == 3:
        pass
    print(k)

# Match Statement -> To perform different actions based on different conditions

day = 5
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tues")
    case 3:
        print("Wed")
    case 4:
        print("Thurs")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case 1 | 2 | 3 | 4 | 5 :
        print("Week Days")
    case 6 | 7 :
        print("Holidays")
    case _:
        print("default")