def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

# Example usage:
print(assign_grade(85))  # Output: 'B'
print(assign_grade(92))  # Output: 'A'
print(assign_grade(76))  # Output: 'C'
print(assign_grade(65))  # Output: 'D'
print(assign_grade(55))  # Output: 'E'
print(assign_grade(45))  # Output: 'F'

