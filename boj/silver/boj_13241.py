a, b = map(int, input().split())

m, M = min(a, b), max(a, b)

for i in range(M, a*b + 1, M):
    if i % m == 0 and i % m == 0:
        print(i)
        break
