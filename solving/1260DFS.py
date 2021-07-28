v, e, start = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

queue = [start] # 1. 넣고
visited = [False] * (v + 1) # 인덱스에 해당하는 vertex 방문 여부
visited[start] = True  # 2. 방문체크
while queue:
    now = stack.pop(0)  # 3. 빼고 +  4. 이동
    print(now, end = ' ')
    for next in graph[now]:
        if not visited[next]:  # 5. 방문확인
            queue.append(next)  # 1. 넣고
            visited[next] = True # 2. 방문체크