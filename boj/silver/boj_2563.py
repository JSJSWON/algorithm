n = int(input())
sq = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x-1, x + 9):
        for j in range(y-1, y + 9):
            if sq[j][i] == 0:
                sq[j][i] = 1
ans = 0
for y in sq:
    for x in y:
        if x == 1:
            ans += 1
print(ans)