numbers = [number for number in range(1, 20)]
print(numbers)

evenNumbers = [number for number in range(1, 20) if number % 2 == 0]
print(evenNumbers)

oddNumbers = [number for number in range(1, 20) if number % 2 != 0]
print(oddNumbers)

multiples_of_3 = [number for number in range(1, 20) if number % 3 == 0]
print(multiples_of_3)

multiples_of_3_or_5 = [number for number in range(1, 20) if number % 3 == 0 or number % 5 == 0]
print(multiples_of_3_or_5)

multiples_of_3_and_5 = [number for number in range(1, 20) if number % 3 == 0 and number % 5 == 0]
print(multiples_of_3_and_5)
