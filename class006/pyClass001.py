def sum_of_squares_upto_limit(limit):
    sum_of_squares = 0
    number = 1
    while number ** 2 <= limit:
        sum_of_squares += number ** 2
        number += 1
    return sum_of_squares


print(sum_of_squares_upto_limit(100))
