try:
    i = 0
    j = 10 / i
except:
    print("Exception caught!")
    j = 0
print(j)

try:
    i = 0
    j = 10 / i
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    j = 0
except Exception as e:
    print(f"An error occurred: {e}")
print(j)


try:
    i = 0
    j = 10 / i
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    j = 0
finally:
    print("This block is always executed.")
print(j)
