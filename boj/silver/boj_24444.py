from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(x) for x in graph]


def bfs():
    queue = deque()
    visited = [0 for _ in range(N + 1)]

    queue.append(R)
    cnt = 1
    while queue:
        t = queue.popleft()
        if visited[t] != 0:
            continue
        visited[t] = cnt
        cnt += 1
        for x in graph[t]:
            if visited[x] == 0:
                queue.append(x)
    return visited


ans = bfs()
for i in range(1, N+1):
    print(ans[i])
