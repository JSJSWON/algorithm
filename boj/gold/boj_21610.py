import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

move = []
for _ in range(M):
    move.append(tuple(map(int, input().split())))

cloud = [[N-1, 1-1], [N-1, 2-1], [N-1-1, 1-1], [N-1-1, 2-1]]
directions = ([0, -1], [-1, -1], [-1, 0], [-1, 1],
              [0, 1], [1, 1], [1, 0], [1, -1])

for m in move:
    d = m[0] - 1
    s = m[1]

    moved = set()
    for c in cloud:
        c[0] = (c[0] + directions[d][0] * s) % N
        c[1] = (c[1] + directions[d][1] * s) % N
        moved.add((c[0], c[1]))
        graph[c[0]][c[1]] += 1

    for c in cloud:
        for i in range(1, len(directions), 2):
            c0 = c[0] + directions[i][0]
            c1 = c[1] + directions[i][1]
            if 0 <= c0 < N and 0 <= c1 < N:
                if graph[c0][c1] > 0:
                    graph[c[0]][c[1]] += 1

    # 아래 새로운 cloud를 지정하면서 not in을 사용하는데
    # 이 부분을 list로 하면 시간초과가 나옴
    # set으로 바꾸니 통과
    cloud = [[i, j] for i in range(N) for j in range(N) if (i, j) not in moved and graph[i][j] >= 2]
    for c in cloud:
        graph[c[0]][c[1]] -= 2


answer = 0
for g in graph:
    answer += sum(g)
print(answer)
