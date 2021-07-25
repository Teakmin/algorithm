import sys
input = sys.stdin.readline

# .rstrip
N = int(input())
stack = []
for _ in range(N):
    line = input().rstrip()
    if line[:4] == "push":
        stack.append(line[5:])
    elif line[:3] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif line[:4] == "size":
        print(len(stack))
    elif line[:5] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif line[:3] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    print(stack)