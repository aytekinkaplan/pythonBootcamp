string = str(input("Enter a string: "))


def finding_character(string):
    for i in range(len(string)):
        print(f"{i + 1}. character", f"is {string[i]} and ascii value is {ord(string[i])}")


finding_character(string)
