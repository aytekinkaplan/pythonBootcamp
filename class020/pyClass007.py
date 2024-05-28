def student_summary(student):
    name, age, grade = student
    return f"Student Name: {name}, Age: {age}, Grade: {grade}"


# Test cases
print(student_summary(('Alice', 20, 89.5)))  # Expected Output: "Student Name: Alice, Age: 20, Grade: 89.5"
print(student_summary(('Bob', 22, 75.8)))  # Expected Output: "Student Name: Bob, Age: 22, Grade: 75.8"
print(student_summary(('Charlie', 19, 92.0)))  # Expected Output: "Student Name: Charlie, Age: 19, Grade: 92.0"
