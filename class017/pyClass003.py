try:
    value = int("42")
    print("Value:", value)
except ValueError as error:
    print("ValueError:", error)
else:
    print("No exception occurred.")
finally:
    print("This will always execute.")

try:
    value = int("not a number")
except ValueError as error:
    print("ValueError:", error)
else:
    print("No exception occurred.")
finally:
    print("This will always execute.")

try:
    file = open("example.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError as error:
    print("File not found:", error)
else:
    print("File read successfully.")
finally:
    if file:
        file.close()
    print("File closed.")
