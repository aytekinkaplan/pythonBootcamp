# Linear Search in Python with Examples
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
result = linear_search(arr, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
