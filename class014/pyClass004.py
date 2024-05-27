queue = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']

print(queue)

while 'Terry' in queue:
    queue.remove('Terry')
print(queue)

queue = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']

queue.remove('Terry')
print(queue)

queue.remove('Terry')
print(queue)

queue.append('Terry')
print(queue)

queue.append('Johnson')
print(queue)

queue.pop(0)
print(queue)

queue.pop(0)
print(queue)

queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']

queue1.extend(queue2)
print(queue1)

queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']

queue1 += queue2
print(queue1)

queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']

queue1 = queue1 + queue2
print(queue1)

# copy() example
queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = queue1.copy()
print(queue2)

# list() example
queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = list(queue1)
print(queue2)

# tuple() example
queue1 = ['Eric', 'John', 'Michael', 'Graham', 'Terry', 'Terry', 'Michael']
queue2 = tuple(queue1)
print(queue2)

