mark1 = 45
mark2 = 55
mark3 = 65
mark4 = 75
mark5 = 85
marks = [mark1, mark2, mark3, mark4, mark5]

total = sum(marks)
print(total)
maxMark = max(marks)
print(maxMark)
minMark = min(marks)
print(minMark)

marks.sort()
print(marks)

marks.reverse()
print(marks)


print(len(marks))


total = sum(marks)
print(total)

average = total / len(marks)
print(average)

marks.append(95)
marks.append(100)

total = sum(marks)
print(total)
average = total / len(marks)
print(average)

print(55 in marks)
print(100 in marks)
print(75 in marks)

for mark in marks:
    print(mark)

marks.insert(3, 60)

for mark in marks:
    print(mark)

marks.remove(60)

for mark in marks:
    print(mark)

marks.pop()

for mark in marks:
    print(mark)

marks.clear()

for mark in marks:
    print(mark)
