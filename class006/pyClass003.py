i = 1
while i < 11:
    print(i)
    if i == 5:
        break
    i += 1

j = 1
while j < 11:
    if j == 5:
        j += 1
        continue
    print(j)
    j += 1
