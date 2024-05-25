# Coding Exercise: Check if a Year is a Leap Year
# Write a program that reads a year and checks if it is a leap year.

year = int(input("Enter a year: "))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(year))
