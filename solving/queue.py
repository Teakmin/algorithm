queue = []

# push
queue.append(1)
print("push 1", queue)
queue.append(2)
print("push 2", queue)
queue.append(3)
print("push 3", queue)

#pop
print("pop", queue.pop(0))
print(queue)


#peek
print("peek", queue[0])
print(queue)

#pop하는데 볼 필요는 없음
del stack[0]
print("del keyword", stack)