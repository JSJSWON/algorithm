import copy
from collections import deque, defaultdict
from itertools import combinations

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def bfs(r, c):  # [r, c]에서의 치킨 거리([r, c]는 집)
    visited = copy.deepcopy(graph)
    queue = deque()
    queue.append([r, c, 0])
    total_dist = dict()
    visited[r][c] = -1
    while queue:
        v = queue.popleft()
        crd = [v[0], v[1]]
        dist = v[2]
        for d in directions:
            if 0 <= crd[0] + d[0] < N and 0 <= crd[1] + d[1] < N:
                if visited[crd[0] + d[0]][crd[1] + d[1]] == -1:
                    continue
                if graph[crd[0] + d[0]][crd[1] + d[1]] == 2:
                    # total_dist.append(dist + 1)
                    total_dist[(crd[0] + d[0], crd[1] + d[1])] = dist + 1
                queue.append([crd[0] + d[0], crd[1] + d[1], dist + 1])
                visited[crd[0] + d[0]][crd[1] + d[1]] = -1

    return total_dist


ans = defaultdict(list)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            tmp = bfs(i, j)
            for item in tmp:
                ans[item].append([tmp[item], [i, j]])
            # ans.append(bfs(i, j))
# print(ans)
answer = 10**8
aa = list(combinations([x for x in range(len(ans))], M))
for aaa in aa:
    index = 0
    cand = defaultdict(list)
    for an in ans:
        if index in aaa:
            for tt in ans[an]:
                cand[tuple(tt[1])].append(tt[0])
        index += 1
    # print(cand)
    if answer > sum([min(cand[x]) for x in cand]):
        answer = sum([min(cand[x]) for x in cand])
    # print(cand)
    # print(sum([min(cand[x]) for x in cand]))
    # print("-===")
print(answer)
