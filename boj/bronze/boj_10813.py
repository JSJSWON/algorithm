N, M = map(int, input().split())

b = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = b[i]
    b[i] = b[j]
    b[j] = tmp

ans = ' '.join(map(str, b[1:]))

print(ans)
