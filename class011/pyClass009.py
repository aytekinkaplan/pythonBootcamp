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
