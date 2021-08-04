v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]  # 0번 인덱스는 사용x, 1~v까지 사용 --> v+1로
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (v + 1)  # 마찬가지로 0번 인덱스는 사용 x
queue = [1] # 시작은 1
visited[1] = True
while queue:
    now = queue.pop(0)

    for next in graph[now]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True

print(sum(visited) - 1)