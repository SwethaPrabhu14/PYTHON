# TRY-EXCEPT-ELSE-FINALLY:
# Exception Handling :

try:
    # test a block of code
    f = open("file.txt", "w")
    f.write("Hello")
except FileNotFoundError:
    # you handle the error
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
else:
    # executes if no exception(error) occurred
    print("File written successfully")
finally:
    # always executes
    f.close()
    print("File closed")

# Raise a Exception :

x = -1
if x < 0:
    raise Exception("Sorry")