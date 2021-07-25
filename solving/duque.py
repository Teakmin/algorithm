from collections import deque

print("=======stack=========")
stack = deque([1, 2])
# stack = deque() #도 가능 (비었다면)
# stack = deque([1, 2]) #(비어있지 않다면 이렇게 써야함)

# stack = []

# push
stack.append(3)
print("push 3", stack)

#pop
print("pop", stack.pop())
print(stack)

#peek
print("peek", stack[-1])
print(stack)

#pop하는데 볼 필요는 없음
del stack[-1]
print("del keyword", stack)

print("=======queue=========")
queue = deque([1, 2])
# queue = deque() #도 가능 (비었다면)
# queue = deque([1, 2]) #(비어있지 않다면 이렇게 써야함)

# queue = []

# push
queue.append(3)
print("push 3", queue)

#pop
print("pop", queue.popleft())
print(queue)

#peek
print("peek", queue[0])
print(queue)

#pop하는데 볼 필요는 없음
del queue[0]
print("del keyword", queue)