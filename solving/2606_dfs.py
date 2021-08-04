v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]  # 0번 인덱스는 사용x, 1~v까지 사용 --> v+1로
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (v + 1)
# 재귀함수 버전
def dfs(graph, visited, now, v):
    visited[now] = True # 4. 방문체크
    for next in graph[now]:
        if not visited[next]:
            dfs(graph, visited,next, v ) # 1. 이동

dfs(graph, visited, 1, v)
print(sum(visited) - 1)