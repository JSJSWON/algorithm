class Solution:
    def fib(self, n: int) -> int:
        ans = [0, 1]
        for i in range(2, n + 1):
            ans.append(ans[i - 1] + ans[i - 2])
        return ans[n]


from collections import defaultdict


class Solution:
    dp = defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        return x
