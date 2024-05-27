number = int(input("Enter a number: "))
def multiplying(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * multiplying(number - 1)


print(multiplying(number))
