nummber = int(input("Enter a number: "))


def summing(number):
    if number == 0:
        return 0
    else:
        return number + summing(number - 1)


print(summing(nummber))
