
v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in graph:
    x.sort()

queue = [start] # 1. 넣고
bfs_visited = [False] * (v + 1) # 인덱스에 해당하는 vertex 방문 여부
bfs_visited[start] = True # 2. 방문체크
while queue:
    now = queue.pop(0) # 3. 빼고 + 4. 이동
    print(now, end=' ')
    for next in graph[now]:
        if not bfs_visited[next]: # 5. 방문확인
            queue.append(next) # 1. 넣고
            bfs_visited[next] = True # 2. 방문체크
print()

stack = [start] # 1. 넣고
dfs_visited = [False] * (v + 1) # 인덱스에 해당하는 vertex 방문 여부
dfs_visited[start] = True # 2. 방문체크
while stack:
    now = stack.pop() # 3. 빼고 + 4. 이동
    print(now, end=' ')
    for next in graph[now][::-1]:
        if not dfs_visited[next]: # 5. 방문확인
            stack.append(next) # 1. 넣고
            dfs_visited[next] = True # 2. 방문체크