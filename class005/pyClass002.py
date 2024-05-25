def is_valid_triangle(angle1, angle2):
    if angle1 + angle2 < 180:
        return "This is a valid triangle"
    else:
        return "This is not a valid triangle"


print(is_valid_triangle(30, 30))
print(is_valid_triangle(30, 31))
print(is_valid_triangle(30, 32))
print(is_valid_triangle(30, 33))


def is_valid_triangle1(angle1, angle2, angle3):
    if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
        return "This is a valid triangle"
    else:
        return "This is not a valid triangle"


print(is_valid_triangle1(30, 30, 30))
print(is_valid_triangle1(30, 30, 31))
print(is_valid_triangle1(30, 30, 32))
print(is_valid_triangle1(30, 30, 33))
print(is_valid_triangle1(30, 40, 50))
print(is_valid_triangle1(50, 60, 70))
print(is_valid_triangle1(90, 90, 90))
