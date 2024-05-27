enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i)

for i, j in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i, j)

for i, j in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10):
    print(i, j)

for i, j in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], start=10):
    print(i, j)
