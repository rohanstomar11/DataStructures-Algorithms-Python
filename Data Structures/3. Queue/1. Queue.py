queue = []

queue.append(11)
queue.append(22)
queue.append(33)

print("Queue")
print(queue)

print('\nElements to be processed from queue:')
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))

print("Queue after elements are processed:")
print(queue)
