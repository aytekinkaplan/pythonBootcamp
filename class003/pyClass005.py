# Calculate factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of", n, "is", fact)

fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("The factorial of", n, "is", fact)


def fact(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact


n = int(input("Enter a number: "))
print("The factorial of", n, "is", fact(n))
