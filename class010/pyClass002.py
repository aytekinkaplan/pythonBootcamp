def two_dimensional(rows, columns):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(columns):
            array[i].append(i * 3 * j + 3)
    return array


array = two_dimensional(10, 10)

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=" ")
    print()
