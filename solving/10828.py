import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().rstrip()
    if command[:4] == "push" : stack.append(command[5:])
    elif command == "size": print(len(stack))
    elif command == "pop":
        if not stack: print(-1)
        else: print(stack.pop())
    elif command == "empty":
        if not stack: print(1)
        else: print(0)
    elif command == "top":
        if not stack: print(-1)
        else: print(stack[-1])
