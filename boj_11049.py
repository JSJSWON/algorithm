N = int(input())
matrix = []
cnt = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

for i in range(1, N):
    for j in range(N):
        if j + i == N:
            break
        if i == 1:
            cnt[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
        else:
            cnt[j][j+i] = 2**31
            for k in range(j, j+i):
                cnt[j][j+i] = min(cnt[j][j+i],
                                  cnt[j][k] + cnt[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(cnt[0][-1])
