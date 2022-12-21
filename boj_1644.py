N = int(input())
dp = [2]
for i in range(3, N+1):
    tmp = 0
    for j in range(2, int(i**(0.5))+ 1):
        if i % j == 0:
            tmp += 1
            break
    if tmp == 0:
        dp.append(i)

left, right, ans, s = 0, 0, 0, dp[0]
while True:
    if s == N:
        ans += 1
        s -= dp[left]
        left += 1
        right += 1
        if right == len(dp):
            break
        s += dp[right]
    elif s < N:
        right += 1
        if right == len(dp):
            break
        s += dp[right]
    else:
        s -= dp[left]
        left += 1

print(ans)