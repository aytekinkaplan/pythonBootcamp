#  Introduction To List Comprehension In Python with Examples

# 1. Create a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]
print(numbers)

# 2. Create a list of numbers from 1 to 10 that are even
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 3. Create a list of numbers from 1 to 10 that are odd
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(odd_numbers)

# 4. Create a list of numbers from 1 to 10 that are multiples of 3
multiples_of_3 = [x for x in range(1, 11) if x % 3 == 0]
print(multiples_of_3)

# 5. Create a list of numbers from 1 to 10 that are multiples of 3 or 5
multiples_of_3_or_5 = [x for x in range(1, 11) if x % 3 == 0 or x % 5 == 0]
print(multiples_of_3_or_5)

# 6. Create a list of numbers from 1 to 10 that are multiples of 3 and 5
multiples_of_3_and_5 = [x for x in range(1, 11) if x % 3 == 0 and x % 5 == 0]
print(multiples_of_3_and_5)

# 7. Create a list of numbers from 1 to 10 that are multiples of 3 or 5
multiples_of_3_or_5 = [x for x in range(1, 11) if x % 3 == 0 or x % 5 == 0]
print(multiples_of_3_or_5)

# 8. Create a list of numbers from 1 to 10 that are multiples of 3 and 5
multiples_of_3_and_5 = [x for x in range(1, 11) if x % 3 == 0 and x % 5 == 0]
print(multiples_of_3_and_5)
