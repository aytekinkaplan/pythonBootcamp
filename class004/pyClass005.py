number = 10

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# Output
# Positive Number

# factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of", n, "is", fact)


# Output
# Enter a number: 5
# The factorial of 5 is 120
