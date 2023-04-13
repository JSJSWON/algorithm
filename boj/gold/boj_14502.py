from itertools import combinations
from copy import deepcopy


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


# 재귀를 이용해 바이러스를 퍼트린 뒤 바이러스 수 세기
def count_virus(graph):
    g = deepcopy(graph)

    def dfs(i: int, j: int):
        if i < 0 or j < 0 or i >= len(g) or j >= len(g[0]) or g[i][j] == 1 or g[i][j] == 2:
            return
        g[i][j] = 2

        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j + 1)

    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 2:
                g[i][j] = 0
                dfs(i, j)

    ans = 0
    for x in g:
        ans += x.count(0)

    return ans


# 0의 위치 중 세 개 선택(조합)
loc_zeros = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            loc_zeros.append([i, j])

loc_zeros_comb = combinations(loc_zeros, 3)
ans = 0

for x in loc_zeros_comb:
    g = deepcopy(graph)
    for i, j in x:
        g[i][j] = 1

    c = count_virus(g)
    if ans < c:
        ans = c
print(ans)
