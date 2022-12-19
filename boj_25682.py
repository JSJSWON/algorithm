n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
# 좌상단이 B일 때 graph[i][j] = 좌상단이 (0,0)이고 우하단이(i,j)인 사각형 내 틀린 개수
block = ['B', 'W']
for i in range(n):
    tmp = input()
    for j in range(m):
        if i == 0:
            if j == 0:
                if tmp[j] == block[(i+j)%2]:
                    graph[i].append(0)
                else:
                    graph[i].append(1)
            else:
                if tmp[j] != block[(i+j)%2]:
                    graph[i].append(graph[i][j-1] + 1)
                else:
                    graph[i].append(graph[i][j-1])
        else:
            if j == 0:
                if tmp[j] == block[(i+j)%2]:
                    graph[i].append(graph[i-1][j])
                else:
                    graph[i].append(graph[i-1][j]+1)
            else:
                if tmp[j] != block[(i+j)%2]:
                    graph[i].append(graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1] + 1)
                else:
                    graph[i].append(graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1])
            
ans = 10**10
for i in range(k-1, n):
    for j in range(k-1, m):
        tmp = graph[i][j]
        if i - k >= 0:
            tmp -= graph[i-k][j]
        if j - k >= 0:
            tmp -= graph[i][j-k]
        if i - k >= 0 and j - k >= 0:
            tmp += graph[i-k][j-k]
        tmp = min(tmp, k*k - tmp)
        if ans > tmp:
            ans = tmp
print(ans)