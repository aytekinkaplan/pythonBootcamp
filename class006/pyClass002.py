def sum_of_cubes_upto_limit(limit):
    sum = 0
    n = 1

    while True:
        cube = n ** 3
        if cube > limit:
            break
        sum += cube
        n += 1

    return sum


# Example usage:
print(sum_of_cubes_upto_limit(30))  # Output: 36
print(sum_of_cubes_upto_limit(100))  # Output: 99 (1 + 8 + 27 + 64)
print(sum_of_cubes_upto_limit(1))  # Output: 1
print(sum_of_cubes_upto_limit(0))  # Output: 0
