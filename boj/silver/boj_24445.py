from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(g, reverse=True) for g in graph]


def bfs(R):
    visited = [0 for _ in range(N + 1)]
    cnt = 1
    queue = deque([R])
    while queue:
        v = queue.popleft()
        if visited[v] != 0:
            continue
        visited[v] = cnt
        cnt += 1
        for x in graph[v]:
            if visited[x] == 0:
                queue.append(x)
    return visited


ans = bfs(R)

for i in range(len(ans)):
    if i == 0:
        continue
    print(ans[i])
