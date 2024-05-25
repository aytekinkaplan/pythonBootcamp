def sum_of_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def print_names(string, sum_of_numbers):
    for name in range(0, sum_of_numbers):
        print(string)


print_names("hello", sum_of_numbers(5))
