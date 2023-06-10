N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])


def move(graph):
    new_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i][j])):
                m, s, d = graph[i][j][k]

                new_i = (i + directions[d][0] * s) % N
                new_j = (j + directions[d][1] * s) % N

                new_graph[new_i][new_j].append([m, s, d])

    return new_graph


def sep(graph):
    new_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if len(graph[i][j]) >= 2:
                new_m = sum([x[0] for x in graph[i][j]]) // 5
                if new_m == 0:
                    continue

                new_s = sum([x[1] for x in graph[i][j]]) // len(graph[i][j])

                tmp = 0  # 방향이 모두 홀수인지 짝수인지 알기 위한 변수
                for x in graph[i][j]:
                    if x[2] % 2 == 0:
                        tmp += 1
                    else:
                        tmp -= 1
                if tmp == len(graph[i][j]) or tmp == -len(graph[i][j]):
                    new_d = 0
                else:
                    new_d = 1

                for k in range(new_d, len(directions), 2):
                    new_graph[i][j].append([new_m, new_s, k])
            else:
                new_graph[i][j] = graph[i][j]
    return new_graph


for _ in range(K):
    graph = move(graph)

    graph = sep(graph)

answer = 0
for g in graph:
    for gg in g:
        for ggg in gg:
            answer += ggg[0]

print(answer)
