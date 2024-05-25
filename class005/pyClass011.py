# Ternary Operator
# Write a program that reads a number and prints "Even" if the number is even, or "Odd" if the number is odd.

number = int(input("Enter a number: "))

print("Even" if number % 2 == 0 else "Odd")

# More Ternary Operator
# Write a program that reads a number and prints "Positive" if the number is positive,
# "Negative" if the number is negative, or "Zero" if the number is zero.

number = int(input("Enter a number: "))

print("Positive" if number > 0 else "Negative" if number < 0 else "Zero")

# Ternary Operator with Multiple Conditions
# Write a program that reads a number and prints "Positive" if the number is positive,
# "Negative" if the number is negative, or "Zero" if the number is zero.

number = int(input("Enter a number: "))

print("Positive" if number > 0 else ("Negative" if number < 0 else "Zero"))


