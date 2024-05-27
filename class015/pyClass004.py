names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
name_results = [name for name in names if 'a' in name]
print(name_results)

even_numbers = [number for number in range(1, 21) if number % 2 == 0]
print(even_numbers)

odd_numbers = [number for number in range(1, 21) if number % 2 != 0]
print(odd_numbers)

multiples_of_3 = [number for number in range(1, 21) if number % 3 == 0]
print(multiples_of_3)

multiples_of_3_or_5 = [number for number in range(1, 21) if number % 3 == 0 or number % 5 == 0]
print(multiples_of_3_or_5)

multiples_of_3_and_5 = [number for number in range(1, 21) if number % 3 == 0 and number % 5 == 0]
print(multiples_of_3_and_5)

