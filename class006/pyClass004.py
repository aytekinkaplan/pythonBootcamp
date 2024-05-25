number = 10
while number > 0:
    print(number)
    number -= 2

# Output:
# 10
# 8
# 6
# 4
# 2

i = 5
while i * i < 10:
    print(i)
    i += 1

# Output:
# 5
# 6
# 7
# 8
# 9

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        break
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

i = 2
while i * i < 10:
    print(i, end=' ')
    i = i + 1
print("done")

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("done")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("done")

for i in range(1, 11):
    if i % 2:
        break
    print(i)
print("done")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("done")
