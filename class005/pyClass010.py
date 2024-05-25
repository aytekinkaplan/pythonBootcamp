def is_right_angled_triangle(side1, side2, side3):
    # Validate that all sides are positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    # Check all possible combinations to see if they satisfy the Pythagorean theorem
    if side1 ** 2 == side2 ** 2 + side3 ** 2:
        return True
    if side2 ** 2 == side1 ** 2 + side3 ** 2:
        return True
    if side3 ** 2 == side1 ** 2 + side2 ** 2:
        return True

    # If none of the combinations satisfy the theorem, it's not a right-angled triangle
    return False


# Example usage:
print(is_right_angled_triangle(3, 4, 5))  # Output: True
print(is_right_angled_triangle(1, 2, 3))  # Output: False
