t = int(input())

for _ in range(t):
    K = int(input())
    Ks = list(map(int, input().split()))

    prefix_sum = [0]
    for x in Ks:
        prefix_sum.append(prefix_sum[-1] + x)
    dp = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

    for i in range(1, K):
        for j in range(1, K):
            if j + i > K:
                break
            tmp = 10**8
            for k in range(i):
                if tmp > dp[j][j+k] + dp[j+k+1][j+i]:
                    tmp = dp[j][j+k] + dp[j+k+1][j+i]

            dp[j][j + i] = tmp + prefix_sum[j + i] - prefix_sum[j - 1]
    print(dp[1][-1])
