n, m = map(int, input().split())
goal = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        goal[index - 1] = k

print(*goal)
