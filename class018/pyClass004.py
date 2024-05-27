s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 - s2
s4 = s2 - s1
s5 = s1 | s2
s6 = s1 & s2
s7 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

result = s1.union(s2)
print(result)

result = s1.intersection(s2)
print(result)

result = s1.difference(s2)
print(result)

result = s2.difference(s1)
print(result)

result = s1.symmetric_difference(s2)
print(result)

result = s1.isdisjoint(s2)
print(result)

result = s1.issubset(s2)
print(result)

result = s1.issuperset(s2)
print(result)