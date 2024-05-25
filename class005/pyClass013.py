marks = int(input("Enter your marks: "))


def assign_grade(marks):
    if marks >= 90:
        return "Your grade is A"
    elif marks >= 80:
        return "Your grade is B"
    elif marks >= 70:
        return "Your grade is C"
    elif marks >= 60:
        return "Your grade is D"
    elif marks >= 50:
        return "Your grade is E"
    else:
        return "Your grade is F"


print(assign_grade(marks))
