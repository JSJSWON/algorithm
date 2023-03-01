N, M = map(int, input().split())

b = [i for i in range(N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    b[i:j + 1] = b[k:j + 1] + b[i:k]

print(' '.join(map(str, b[1:])))
