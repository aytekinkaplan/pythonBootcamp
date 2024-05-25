# Finding the Next Fibonacci Number Exceeding a Threshold

# Write a program that finds the next Fibonacci number that exceeds a given threshold.

def find_fibonacci_exceeding_threshold(threshold):
    a, b = 0, 1
    while b <= threshold:
        a, b = b, a + b
    return b


# Example usage:
print(find_fibonacci_exceeding_threshold(100))  # Output: 354224848179261915075
print(find_fibonacci_exceeding_threshold(50))  # Output: 12586269025
