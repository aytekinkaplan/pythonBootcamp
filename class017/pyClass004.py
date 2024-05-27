try:
    # Code that may raise an exception
    x = int("not a number")
except ValueError:
    print("ValueError: Invalid literal for int()")
except TypeError:
    print("TypeError: Incorrect type")

try:
    x = int("42")
except ValueError:
    print("ValueError: Invalid literal for int()")
else:
    print("No exception occurred.")

try:
    i = 0  # Simulating input from user
    j = 10 / i
finally:
    print("Finally")  # This line will be executed

# This line will NOT be executed because an exception is raised and not caught
print("End")

try:
    i = 1  # Change this value to 0 to raise an exception
    j = 10 / i
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
    j = 0
except TypeError:
    print("Caught TypeError")
else:
    print("No exceptions occurred")
finally:
    print("Finally block executed")

print("Value of j:", j)
