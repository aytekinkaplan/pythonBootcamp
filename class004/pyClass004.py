from decimal import Decimal

# Create a decimal number with 2 decimal places of precision
number = Decimal('1.23')

number = number + Decimal('0.01')
print(number)

number = number - Decimal('0.01')
print(number)

number = number * Decimal('0.01')
print(number)

number = number / Decimal('0.01')
print(number)

value1 = Decimal('4.5')
print(value1)
value2 = Decimal('3.2')
print(value2)
result = value1 - value2
print(result)  # Decimal('1.3')
