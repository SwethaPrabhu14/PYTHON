# Operators

a = 20
b = 5
str = " Swetha Lokeshwaran "

# 1. Arithmetic -> [+, -, *, /, %, **, //]
print("Arithmetic Operators:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# 2. Assignment -> [=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=]
print("Assignment Operators:")
print(a)
a += b; print(a)
a -= b; print(a)
a *= b; print(a)
a /= b; print(a)
a %= b; print(a)
a **= b; print(a)
a //= b; print(a)

# 3. Comparsion -> [==, !=, >, <, >=, <=]
print("Comparsion Operators:")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 4. Logical -> [and, or, not]
print("Logical Operators:")
print ((a > b) and (a < b))
print ((a > b) or (a < b))
print (not(a > b))

# 5. Identity -> [is, is not]
print("Identity Operators:")
print(str == "Swetha")
print(str != "lokesh")

# 6. Membership -> [in, not in]
print("Membership Operators:")
print("Swetha" in str)
print("Swetha" not in str)

# 7. Bitwise -> [&, |, ^, ~, <<, >>]
print("Bitwise Operators:")
print(10 & 5)
print(10 | 5)
print(10 ^ 5)
print(~10)
print(10 << 5)
print(10 >> 5)