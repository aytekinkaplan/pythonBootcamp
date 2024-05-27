def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value


# Test the function
result = find_max(3, 8, 2, 10, 5)
print(result)  # Outputs: 10


def combine_strings(*args):
    return ' '.join(args)


# Test the function
result = combine_strings('Hello', 'world', 'from', 'Python')
print(result)  # Outputs: Hello world from Python


def sum_numbers(*args):
    return sum(args)


# Test the function
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Outputs: 15


def print_args(*args):
    for arg in args:
        print(arg)


# Test the function
print_args('apple', 'banana', 'cherry')


# Outputs:
# apple
# banana
# cherry

def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")


# Test the function
greet('Hello', 'Alice', 'Bob', 'Charlie')
# Outputs:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
