T = int(input())
dp = [[i for i in range(1, 15)]]
for i in range(1, 15):
    dp.append([])
    s = dp[i-1][0]
    for j in range(14):
        dp[i].append(s)
        if j != 13:
            s += dp[i-1][j+1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])
