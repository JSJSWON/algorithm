import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**10)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

visited = [0 for _ in range(N+1)]
visited[R] = 1
cnt = 1


def dfs(v):
    global cnt
    visited[v] = cnt
    for g in graph[v]:
        if visited[g] == 0:
            cnt += 1
            dfs(g)


dfs(R)

for i in range(1, N+1):
    print(visited[i])
