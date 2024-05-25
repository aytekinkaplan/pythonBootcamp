# Coding Exercise: Are Both Numbers Even
# Write a program that reads two numbers and checks if both of them are even.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))


def are_both_numbers_even(number1, number2):
    if number1 % 2 == 0 and number2 % 2 == 0:
        return True
    else:
        return False


print(are_both_numbers_even(number1, number2))
