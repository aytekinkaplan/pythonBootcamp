def calculate_sum_of_divisors(number):
    # Initialize sum_of_divisors to 0
    sum_of_divisors = 0

    # If the number is less than or equal to 0, return 0
    if number <= 0:
        return sum_of_divisors

    # Loop through all numbers from 1 to number (inclusive)
    for i in range(1, number + 1):
        # If i is a divisor of number, add it to sum_of_divisors
        if number % i == 0:
            sum_of_divisors += i

    # Return the sum of divisors
    return sum_of_divisors


# Example usage
print(calculate_sum_of_divisors(15))  # Output: 24

