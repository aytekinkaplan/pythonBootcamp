def common_subjects(grade1, grade2, grade3):
    # Check if any grade is empty
    if not grade1 or not grade2 or not grade3:
        return set()

    # Function to find common subjects in a grade
    def common_in_grade(grade):
        if not grade:
            return set()

        # Initialize common subjects with the subjects of the first student
        common = set(next(iter(grade.values())))

        # Intersect with the subjects of all other students
        for subjects in grade.values():
            common.intersection_update(subjects)

        return common

    # Find common subjects in each grade
    common1 = common_in_grade(grade1)
    common2 = common_in_grade(grade2)
    common3 = common_in_grade(grade3)

    # Find intersection of common subjects across all three grades
    return common1.intersection(common2, common3)


# Example usage
grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": set(), "Hank": {"History"}}

print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()

