stack = []

# push
stack.append(1)
print("push 1", stack)
stack.append(2)
print("push 2", stack)
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