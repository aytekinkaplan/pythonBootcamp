def calculate_third_angle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    return angle3


print(calculate_third_angle(90, 30))


def sum_of_squares(n):
    sum = 0
    for i in range(2, 2 * n + 1, 2):
        sum += i ** 2
    return sum


print(sum_of_squares(5))
