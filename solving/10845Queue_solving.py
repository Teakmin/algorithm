from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().rstrip()

    if command[:4] == "push":
        queue.append(command[5:])
    elif command[:3] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command[:4] == "size":
        print(len(queue))
    elif command[:5] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command[:5] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[:4] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])