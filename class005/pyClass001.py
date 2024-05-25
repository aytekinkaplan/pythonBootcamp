def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return "This is a valid triangle"
    else:
        return "This is not a valid triangle"


print(is_valid_triangle(3, 4, 5))
print(is_valid_triangle(3, 4, 6))
print(is_valid_triangle(3, 4, 7))
print(is_valid_triangle(3, 4, 8))

