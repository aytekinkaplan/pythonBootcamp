def is_perfect_number(number):
    if number <= 0:
        return False
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number


# Input
number = int(input("Enter a number: "))

# Process and Output
if is_perfect_number(number):
    print("This is a perfect number")
else:
    print("This is not a perfect number")
