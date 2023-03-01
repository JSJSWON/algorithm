N, M = map(int, input().split())

b = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    b[i:j+1] = b[j:i-1:-1]

print(' '.join(map(str, b[1:])))
