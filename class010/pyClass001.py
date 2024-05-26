def two_dimensional_sum(array):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            sum += array[i][j]
    return sum


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(two_dimensional_sum(array))
