from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(101)]
check = []
visited = [100 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)
    check.append(x)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    check.append(u)

queue = deque([1])
visited[1] = 0

while queue:
    v = queue.popleft()
    if v == 100:
        print(visited[100])
        break
    for x in graph[v]:
        if visited[x] > visited[v]:
            visited[x] = min(visited[x], visited[v])
            queue.append(x)
    for x in range(v+1, v+7):
        if x > 100:
            break
        if visited[x] > visited[v] + 1:
            if x in check:
                # 사다리나 뱀이 있는 곳은 세줄 필요가 없겠지 -> 바로 다른 공간으로 넘어가 버리니까
                visited[graph[x][0]] = min(visited[graph[x][0]], visited[v] + 1)
                queue.append(graph[x][0])
                continue
            visited[x] = min(visited[x], visited[v] + 1)
            queue.append(x)
